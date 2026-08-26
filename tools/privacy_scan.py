"""Fail if public code/data contains known private-project terms or credential-like patterns."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = [ROOT/'src', ROOT/'data', ROOT/'sql', ROOT/'examples']
patterns = {
    'private project naming': re.compile(r'area\s*8|wasfaty|hunger\s*station', re.I),
    'credential labels': re.compile(r'api[_ -]?key|password\s*=|connection\s*string|secret\s*=', re.I),
    'private-network address': re.compile(r'\b(?:10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)\b'),
    'national-id wording': re.compile(r'national\s*id', re.I),
}
issues=[]
for folder in SCAN_DIRS:
    for p in folder.rglob('*'):
        if not p.is_file() or p.suffix.lower() in {'.png','.jpg','.jpeg','.zip'}: continue
        text=p.read_text(encoding='utf-8', errors='ignore')
        for label,rx in patterns.items():
            for m in rx.finditer(text): issues.append((p.relative_to(ROOT),label,m.group(0)))
if issues:
    for item in issues: print('FAIL:', *item)
    sys.exit(1)
print('Privacy scan passed: no blocked private-project terms or credential-like patterns found in public code/data.')
