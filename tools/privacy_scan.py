"""Fail on publication-sensitive identifiers, data, paths, credentials, or branding."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP = {ROOT / ".git", ROOT / "node_modules", ROOT / "src-tauri" / "target"}
TEXT_EXT = {".md", ".html", ".js", ".mjs", ".py", ".sql", ".json", ".toml", ".rs", ".yml", ".yaml", ".txt"}
patterns = {
    "private area identifier": re.compile(r"\barea\s*\d+\b", re.I),
    "legacy branch-domain label": re.compile(r"\bpharmac(?:y|ies)\b", re.I),
    "legacy service-domain label": re.compile(r"\bwasf(?:aty|ty)\b", re.I),
    "legacy delivery brand": re.compile(r"\bhunger\s*station\b", re.I),
    "embedded logo/image": re.compile(r"data:image|base64,|<img[^>]+brandlogo", re.I),
    "credential assignment": re.compile(r"(?:api[_ -]?key|password|secret|token)\s*[:=]\s*['\"][^'\"]+", re.I),
    "private path": re.compile(r"(?:[A-Z]:\\Users\\|/home/[^/]+/|[A-Z]:\\[^\r\n]*Area\d)", re.I),
    "private network": re.compile(r"\b(?:10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)\b"),
}
issues = []
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in TEXT_EXT or any(parent in path.parents for parent in SKIP):
        continue
    if path.is_relative_to(ROOT / "app" / "vendor"):
        continue
    if path.name in {"privacy_scan.py", "INITIAL_PORTFOLIO_README.md"}:
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    for label, pattern in patterns.items():
        for match in pattern.finditer(text):
            issues.append((path.relative_to(ROOT), label, match.group(0)[:80]))
if issues:
    for issue in issues:
        print("FAIL:", *issue)
    sys.exit(1)
print("Publication scan passed: no blocked identifiers, branding, credentials, private paths, or networks.")
