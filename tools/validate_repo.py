"""Portfolio-only structural, source, version, link, and artifact validation."""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "Regional_Sales_Performance_V12_PORTFOLIO.html"
APP = ROOT / "app" / "index.html"

required = [
    "README.md", "LICENSE", ".gitignore", "PUBLICATION_ALLOWLIST.md",
    "PUBLICATION_DENYLIST.md", "SANITIZATION_MANIFEST.md", "package.json",
    "package-lock.json", "src-tauri/Cargo.toml", "src-tauri/Cargo.lock",
    "src-tauri/tauri.conf.json", "tools/prepare_app.mjs",
    "source/Regional_Sales_Performance_V12_PORTFOLIO.html", "app/index.html",
    "docs/analytical_methodology/page-catalog.md",
    "docs/kpi_dictionary/KPI_DICTIONARY.md", "docs/recovery/methodology.md",
    "docs/delivery_channel/methodology.md", "docs/data_quality/rules.md",
    "docs/export/xlsx-export.md", "tests/test_analytics.py", "tests/test_source.py",
]
missing = [item for item in required if not (ROOT / item).exists()]
if missing:
    raise SystemExit("Missing required files:\n- " + "\n- ".join(missing))

package = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
tauri = json.loads((ROOT / "src-tauri" / "tauri.conf.json").read_text(encoding="utf-8"))
cargo = (ROOT / "src-tauri" / "Cargo.toml").read_text(encoding="utf-8")
if package["version"] != "1.0.2" or tauri["version"] != "1.0.2" or not re.search(r'^version = "1\.0\.2"$', cargo, re.MULTILINE):
    raise SystemExit("Version consistency failed; expected 1.0.2.")

html = SOURCE.read_text(encoding="utf-8")
app = APP.read_text(encoding="utf-8")
block = re.search(r"const\s+PAGE_META\s*=\s*\[([\s\S]*?)\];", html)
pages = len(re.findall(r"^\s*\['", block.group(1), re.MULTILINE)) if block else 0
if pages != 18:
    raise SystemExit(f"Expected 18 PAGE_META entries; found {pages}.")
if "portfolio-desktop-safe-area" not in app or "cdn.jsdelivr.net/npm" in app:
    raise SystemExit("Generated desktop frontend is not offline-safe.")
for vendor in ("vendor/xlsx.bundle.js", "vendor/chart.umd.js", "vendor/chartjs-plugin-datalabels.js"):
    if vendor not in app or not (ROOT / "app" / vendor).exists():
        raise SystemExit(f"Missing local desktop dependency: {vendor}")

manifest_path = ROOT / "app" / "generation-manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
app_hash = hashlib.sha256(APP.read_bytes()).hexdigest()
if manifest != {"sourceSha256": source_hash, "appSha256": app_hash, "pageCount": 18, "version": "1.0.2"}:
    raise SystemExit("Generated frontend manifest does not match source/app hashes.")

script_match = re.search(r"<script>([\s\S]*)</script>", html)
if not script_match:
    raise SystemExit("No inline analytical script found.")
with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as handle:
    handle.write(script_match.group(1))
    script_path = Path(handle.name)
try:
    result = subprocess.run(["node", "--check", str(script_path)], capture_output=True, text=True)
    if result.returncode:
        raise SystemExit(result.stderr)
finally:
    script_path.unlink(missing_ok=True)

prohibited_dirs = [ROOT / "node_modules", ROOT / "target", ROOT / "src-tauri" / "target", ROOT / "data", ROOT / "screenshots"]
found_dirs = [str(path.relative_to(ROOT)) for path in prohibited_dirs if path.exists()]
prohibited_ext = {".csv", ".xlsx", ".xls", ".exe", ".msi", ".pdb", ".map", ".zip", ".7z"}
found_files = [str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if ".git" not in path.parts and path.is_file() and path.suffix.lower() in prohibited_ext]
if found_dirs or found_files:
    raise SystemExit(f"Prohibited artifacts found: {found_dirs + found_files}")

link_rx = re.compile(r"\[[^]]+\]\(([^)]+)\)")
broken = []
for doc in [ROOT / "README.md", *ROOT.joinpath("docs").rglob("*.md")]:
    if doc.name == "INITIAL_PORTFOLIO_README.md":
        continue
    text = doc.read_text(encoding="utf-8")
    for target in link_rx.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        clean = target.split("#", 1)[0]
        if clean and not (doc.parent / clean).resolve().exists():
            broken.append(f"{doc.relative_to(ROOT)} -> {target}")
if broken:
    raise SystemExit("Broken Markdown links:\n- " + "\n- ".join(broken))

print("Repository validation passed: 18 pages, version 1.0.2, generated frontend, artifacts, syntax, and links.")
