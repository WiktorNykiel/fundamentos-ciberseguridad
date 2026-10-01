#!/usr/bin/env python3
"""Build and mount the existing DPD site without changing its source or campus output."""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from html.parser import HTMLParser

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREFIX = '/introduccion-dpd'
ORIGIN = 'https://smartkea.com'
SKIP = {'_headers', '_redirects', '.awesome-generated', 'SHA256SUMS.txt', 'sitemap.xml', '_release.json'}
ALLOWED = {'.html', '.css', '.js', '.json', '.md', '.txt', '.svg', '.png', '.ico', '.webp', '.woff2'}

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('a', 'link', 'script', 'img'):
            target = attrs.get('href') if tag in ('a', 'link') else attrs.get('src')
            if target: self.links.append(target)

def validate_site(site: Path) -> None:
    if not (site / 'index.html').is_file(): raise ValueError('Missing index.html')
    for file in site.rglob('*.html'):
        parser = Links(); parser.feed(file.read_text('utf-8'))
        page = ORIGIN + PREFIX + '/' + file.relative_to(site).as_posix()
        for target in parser.links:
            if target.startswith(('#', 'https://', 'mailto:', 'tel:')): continue
            parts = urlsplit(target)
            if parts.scheme or parts.netloc: raise ValueError(f'Unsafe URL in {file.name}')
            resolved = urlsplit(urljoin(page, target)).path
            if not resolved.startswith(PREFIX + '/'): raise ValueError(f'Link escapes prefix: {target}')
            local = site / resolved[len(PREFIX) + 1:]
            if resolved.endswith('/'): local = local / 'index.html'
            if not local.is_file(): raise ValueError(f'Missing target: {target} in {file.name}')

def find_source() -> Path:
    for candidate in (ROOT / 'awesome-dpd', ROOT):
        if (candidate / 'build.py').is_file() or (candidate / 'tools/render.py').is_file(): return candidate
    raise ValueError('No DPD builder. Reconcile/import awesome-dpd sources first.')

def compile_source(source: Path) -> Path:
    if (source / 'build.py').is_file():
        subprocess.run([sys.executable, str(source / 'build.py')], cwd=source, check=True)
        return source / 'dist'
    if (source / 'tools/render.py').is_file():
        subprocess.run([sys.executable, str(source / 'tools/render.py')], cwd=source, check=True)
        return source / 'site'
    raise ValueError('Unsupported source tree')

def mount(source: Path, output: Path, commit: str = 'uncommitted') -> dict:
    if source.is_symlink() or output.is_symlink(): raise ValueError('Symlink directory')
    if any(p.is_symlink() for p in source.rglob('*')): raise ValueError('Symlink asset')
    if output.exists() and not (output / '.dpd-generated').is_file():
        raise ValueError('Refusing to replace an unmarked directory')
    if output.exists() and any(p.is_symlink() for p in output.rglob('*')):
        raise ValueError('Symlink in old output')
    if not re.fullmatch(r'[0-9a-f]{40}|uncommitted', commit): raise ValueError('Invalid source commit')
    temp = Path(tempfile.mkdtemp(prefix='.dpd-build-', dir=output.parent))
    try:
        site = temp / PREFIX.lstrip('/'); site.mkdir()
        for src in sorted(source.rglob('*')):
            if not src.is_file(): continue
            rel = src.relative_to(source)
            if src.name in SKIP or any(p.startswith('.') for p in rel.parts): continue
            if src.suffix.lower() not in ALLOWED: raise ValueError(f'Unexpected public file: {rel}')
            if not re.fullmatch(r'[A-Za-z0-9_./-]+', rel.as_posix()): raise ValueError('Unsafe asset name')
            dest = site / rel; dest.parent.mkdir(parents=True, exist_ok=True)
            if src.suffix == '.html':
                text = src.read_text('utf-8').replace('href="/"', f'href="{PREFIX}/"')
                canonical = ORIGIN + PREFIX + '/' + ('' if rel.as_posix() == 'index.html' else rel.as_posix())
                if not re.search(r'rel=["\']canonical["\']', text, re.I):
                    tag = '<link rel="canonical" href="' + html.escape(canonical, quote=True) + '">'
                    text = text.replace('</head>', tag + '</head>')
                dest.write_text(text, 'utf-8')
            else: shutil.copyfile(src, dest)
        validate_site(site)
        rows = [{'path': p.relative_to(site).as_posix(), 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                for p in sorted(site.rglob('*')) if p.is_file()]
        digest = hashlib.sha256(json.dumps(rows, sort_keys=True).encode()).hexdigest()
        report = {'application': 'introduccion-dpd', 'prefix': PREFIX, 'sourceCommit': commit,
                  'treeSha256': digest, 'files': len(rows), 'deploymentVerified': False}
        (site / '_release.json').write_text(json.dumps(report, indent=2) + '\n')
        (temp / '.dpd-generated').write_text('dpd-public-v1\n')
        if output.exists(): shutil.rmtree(output)
        temp.rename(output)
        return report
    except BaseException:
        shutil.rmtree(temp, ignore_errors=True); raise

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path)
    parser.add_argument('--site', type=Path, help='Already built site; skip executing a source builder')
    args = parser.parse_args()
    try:
        sha = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()
        dirty = subprocess.run(['git', 'status', '--porcelain'], cwd=ROOT, text=True, capture_output=True, check=True).stdout.strip()
        if dirty: sha = 'uncommitted'
    except (subprocess.CalledProcessError, FileNotFoundError): sha = 'uncommitted'
    source = args.site.resolve() if args.site else compile_source((args.source or find_source()).resolve())
    print(json.dumps(mount(source, HERE / 'public', sha), indent=2))
if __name__ == '__main__': main()
