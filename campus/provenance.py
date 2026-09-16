"""Attribute a build only to an identified clean checkout, including new inputs."""
from pathlib import Path
import re
import subprocess


def source_commit(root: Path) -> str | None:
    """Check before producing output. Unknown/dirty Git state is never a clean SHA.

    Ignored build products do not invalidate the source checkout. Untracked files
    do: the compiler may include a new Markdown or laboratory source file. A CI
    environment variable alone cannot prove that its checkout is unchanged.
    """
    options = dict(cwd=root, check=True, capture_output=True, text=True, timeout=5)
    try:
        status = subprocess.run(['git', 'status', '--porcelain=v1', '--untracked-files=all'], **options)
        if status.stdout.strip():
            return None
        head = subprocess.run(['git', 'rev-parse', 'HEAD'], **options).stdout.strip()
        return head if re.fullmatch(r'[0-9a-f]{40}', head) else None
    except (OSError, subprocess.SubprocessError):
        return None
