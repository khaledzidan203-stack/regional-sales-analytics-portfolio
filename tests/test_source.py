import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source" / "Regional_Sales_Performance_V12_PORTFOLIO.html"
APP = ROOT / "app" / "index.html"
MANIFEST = ROOT / "app" / "generation-manifest.json"
PAGE_CATALOG = ROOT / "docs" / "analytical_methodology" / "page-catalog.md"


class SourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = SOURCE.read_text(encoding="utf-8")
        cls.app = APP.read_text(encoding="utf-8")

    def test_18_pages_present(self):
        block = re.search(r"const\s+PAGE_META\s*=\s*\[([\s\S]*?)\];", self.html)
        self.assertIsNotNone(block)
        self.assertEqual(
            len(re.findall(r"^\s*\['", block.group(1), re.MULTILINE)),
            18,
        )

    def test_page_catalog_matches_source_page_count(self):
        catalog = PAGE_CATALOG.read_text(encoding="utf-8")
        catalog_rows = re.findall(r"^\|\s*\d+\s*\|", catalog, re.MULTILINE)
        self.assertEqual(len(catalog_rows), 18)

    def test_required_architectures_present(self):
        for marker in (
            "Strict Comparable Branches",
            "Expected Post",
            "Estimated Sales Recovery",
            "Core Retail ex-Delivery",
            "Data Quality",
            "book_append_sheet",
            "SEARCHABLE_SELECT_IDS",
            "CHART_FILTERS",
        ):
            self.assertIn(marker, self.html)

    def test_generalized_source_has_no_embedded_brand_asset(self):
        embedded_image = r"data:" + r"image|" + r"base" + r"64,"
        self.assertNotRegex(self.html, embedded_image)
        legacy_terms = (
            "Area" + " " + "8",
            "Was" + "faty",
            "Hunger" + " " + "Station",
            "Phar" + "macy",
        )
        for term in legacy_terms:
            self.assertNotIn(term, self.html)
        self.assertNotRegex(
            self.html,
            r"(?i)\barea\s*\d+\b|\bpharmac(?:y|ies)\b",
        )

    def test_generated_app_is_offline_safe(self):
        self.assertNotIn("cdn.jsdelivr.net/npm", self.app)
        for vendor in (
            "vendor/xlsx.bundle.js",
            "vendor/chart.umd.js",
            "vendor/chartjs-plugin-datalabels.js",
        ):
            self.assertIn(vendor, self.app)
            self.assertTrue((ROOT / "app" / vendor).exists())

    def test_generation_manifest_matches_current_source_and_app(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        source_hash = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
        app_hash = hashlib.sha256(APP.read_bytes()).hexdigest()

        self.assertEqual(manifest["sourceSha256"], source_hash)
        self.assertEqual(manifest["appSha256"], app_hash)
        self.assertEqual(manifest["pageCount"], 18)
        self.assertEqual(manifest["version"], "1.0.2")

    def test_versions(self):
        package = json.loads((ROOT / "package.json").read_text())
        tauri = json.loads((ROOT / "src-tauri" / "tauri.conf.json").read_text())
        cargo = (ROOT / "src-tauri" / "Cargo.toml").read_text()

        self.assertEqual(package["version"], "1.0.2")
        self.assertEqual(tauri["version"], "1.0.2")
        self.assertRegex(cargo, r'version = "1\.0\.2"')


if __name__ == "__main__":
    unittest.main()
