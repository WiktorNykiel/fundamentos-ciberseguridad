#!/usr/bin/env python3
"""Build and validate the static campus before an explicit Cloudflare action.

`build`, `check` and `plan` need no network or account. `dry-run` downloads the
pinned Wrangler CLI when absent but does not upload. `deploy` changes production;
`preview` uploads a version without promoting it. No shell or content execution.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from check_release import validate

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CONFIG = ROOT / 'wrangler.jsonc'
WRANGLER = '4.132.0'


def check_config(path: Path = CONFIG) -> dict:
    """Fail closed if this static-only configuration drifts into another app."""
    if path.is_symlink() or not path.is_file():
        raise ValueError('Falta wrangler.jsonc regular en la raíz del repositorio.')
    config = json.loads(path.read_text(encoding='utf-8'))
    allowed = {'name', 'compatibility_date', 'assets'}
    if set(config) != allowed or config['name'] != 'fundamentos-ciberseguridad':
        raise ValueError('Configuración ajena al campus estático; revisa nombre y campos.')
    if config['assets'] != {'directory': './campus/dist', 'not_found_handling': '404-page'}:
        raise ValueError('Los activos deben ser campus/dist, sin backend ni bindings.')
    from datetime import date
    date.fromisoformat(config['compatibility_date'])
    return config


def wrangler_args(action: str) -> list[str]:
    actions = {'dry-run': ['deploy', '--dry-run', '--outdir', str(HERE/'qa/wrangler-dry-run')],
               'deploy': ['deploy'], 'preview': ['versions', 'upload']}
    if action not in actions:
        raise ValueError('Acción de Wrangler no admitida.')
    return ['--yes', f'wrangler@{WRANGLER}', *actions[action], '--config', str(CONFIG)]


def execute(command: list[str], *, timeout: int = 900) -> None:
    """Only fixed commands and repository paths; never interpolate input in a shell."""
    env = dict(os.environ, WRANGLER_SEND_METRICS='false')
    subprocess.run(command, cwd=ROOT, env=env, check=True, timeout=timeout, shell=False)


def build_and_check() -> dict:
    check_config()
    execute([sys.executable, str(HERE/'build.py')])
    report = validate(HERE/'dist', HERE/'pages-ready.zip')
    if not (HERE/'dist/404.html').is_file():
        raise ValueError('Falta la página 404 del campus.')
    print(json.dumps(report, ensure_ascii=False), flush=True)
    return report


def run(action: str) -> int:
    check_config()
    if action == 'plan':
        print(json.dumps({'root': str(ROOT), 'assets': 'campus/dist',
            'wrangler': WRANGLER, 'publishes': False,
            'production': ['npx', *wrangler_args('deploy')],
            'preview': ['npx', *wrangler_args('preview')]}, ensure_ascii=False, indent=2))
        return 0
    if action == 'check':
        print(json.dumps(validate(HERE/'dist', HERE/'pages-ready.zip'), ensure_ascii=False))
        return 0
    build_and_check()
    if action == 'build':
        return 0
    npx = shutil.which('npx')
    if not npx:
        raise ValueError('Node.js/npm con npx son necesarios para Wrangler, no para compilar el curso.')
    if action == 'deploy':
        print('Acción solicitada: publicar el campus en producción.', flush=True)
    elif action == 'preview':
        print('Acción solicitada: subir versión de prueba; no promover producción.', flush=True)
    execute([npx, *wrangler_args(action)])
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['build', 'check', 'plan', 'dry-run', 'deploy', 'preview'])
    args = parser.parse_args()
    try:
        return run(args.action)
    except subprocess.CalledProcessError as error:
        print(f'Fallo del paso de preparación/publicación (código {error.returncode}).', file=sys.stderr)
        return error.returncode if 0 < error.returncode < 126 else 1
    except (ValueError, OSError, subprocess.TimeoutExpired) as error:
        print(f'No se completó la acción: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
