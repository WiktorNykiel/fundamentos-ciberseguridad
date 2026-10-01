#!/usr/bin/env python3
"""Offline structure/link validation. Does not assert legal currency or accreditation."""
from __future__ import annotations
from pathlib import Path
from urllib.parse import urlsplit, unquote
from datetime import date
import json,re
ROOT=Path(__file__).resolve().parents[1]

def load(root:Path=ROOT):
    sources=json.loads((root/'data/sources.json').read_text('utf-8'))
    certs=json.loads((root/'data/certifications.json').read_text('utf-8'))
    if sources.get('schema')!=1 or certs.get('schema')!=1: raise ValueError('Unsupported schema')
    return sources,certs

def validate(root:Path=ROOT)->dict:
    if root.is_symlink(): raise ValueError('Symlink root is not allowed')
    for path in root.rglob('*'):
        if 'site' not in path.relative_to(root).parts and path.is_symlink():
            raise ValueError('Symlink source is not allowed')
    sources,certs=load(root); ids=set(); urls=set()
    for s in sources['sources']:
        if not re.fullmatch(r'[A-Z][A-Z0-9-]+',s['id']) or s['id'] in ids: raise ValueError('Duplicate/invalid source ID')
        ids.add(s['id']); u=urlsplit(s['url'])
        if u.scheme!='https' or not u.hostname or u.username or u.password or u.port not in (None,443): raise ValueError('Unsafe source URL')
        if s['url'] in urls: raise ValueError('Duplicate source URL')
        urls.add(s['url'])
        if date.fromisoformat(s['reviewed_at'])>date.today(): raise ValueError('Future review date')
        if s['review_status'] not in ('revisada','enlace-oficial'):raise ValueError('Review status missing')
        for field in ('title','annotation','category','jurisdiction','language'):
            if not isinstance(s[field],str) or not s[field].strip(): raise ValueError('Empty '+field)
    cids=set()
    for c in certs['certifications']:
        if c['id'] in cids: raise ValueError('Duplicate credential ID')
        cids.add(c['id'])
        if c['source'] not in ids or c['eligibility_source'] not in ids: raise ValueError('Missing credential source')
        if c['mandatory'] is not False: raise ValueError('Credentials must remain optional in these study paths')
        for field in ('name','eligibility','caution','price'):
            if not c[field].strip():raise ValueError('Missing credential conditions')
    for p in root.rglob('*.md'):
        if 'site' in p.relative_to(root).parts:continue
        for link in re.findall(r'\]\(([^)]+)\)',p.read_text('utf-8')):
            if link.startswith(('https://','#','mailto:')):continue
            path=unquote(link.split('#')[0].split('?')[0]);target=(p.parent/path).resolve()
            if not target.is_relative_to(root.resolve()) or not target.is_file():raise ValueError(f'Broken/escaping local link: {p.relative_to(root)} -> {link}')
    return {'status':'passed','sources':len(ids),'certifications':len(cids),'templates':len(list((root/'plantillas').glob('[0-9]*.md'))),'network_checks':False,'legal_review_complete':False}
if __name__=='__main__':print(json.dumps(validate(),ensure_ascii=False,indent=2))
