import tempfile
import unittest
import zipfile
from datetime import date
from pathlib import Path

from tools.analytics_core import (
    budget_gap, core_retail_ex_delivery, estimated_recovery, expected_post,
    is_strict_comparable, lfl_growth, parse_sales_csv, total_sales,
    weighted_ast, write_test_workbook,
)


class AnalyticsTests(unittest.TestCase):
    def test_total_sales_and_delivery_non_double_counting(self):
        recorded = total_sales(100, 20)
        self.assertEqual(recorded, 120)
        self.assertEqual(core_retail_ex_delivery(100, 10), 90)
        self.assertEqual(recorded, total_sales(100, 20))

    def test_weighted_ast_and_budget_gap(self):
        self.assertEqual(weighted_ast(1000, 10), 100)
        self.assertEqual(budget_gap(900, 1000), -100)

    def test_lfl_alignment_formula(self):
        self.assertAlmostEqual(lfl_growth(120, 100), 0.20)

    def test_strict_comparable_exclusions(self):
        windows = [(date(2025, 1, 1), date(2025, 1, 31)), (date(2026, 1, 1), date(2026, 1, 31))]
        self.assertTrue(is_strict_comparable(date(2024, 1, 1), None, windows))
        self.assertFalse(is_strict_comparable(date(2025, 6, 1), None, windows))
        self.assertFalse(is_strict_comparable(date(2024, 1, 1), date(2025, 12, 31), windows))

    def test_recovery_scenario(self):
        expected = expected_post(1000, -0.20)
        self.assertEqual(expected, 800)
        self.assertEqual(estimated_recovery(900, expected), 100)

    def test_priority_quality_rule(self):
        row = {"Core Retail Sales": 100, "Priority Sales": 110}
        self.assertGreater(row["Priority Sales"], row["Core Retail Sales"])

    def test_temporary_csv_parsing(self):
        text = "Date,Branch,Core Retail Sales,Service Channel Sales,Priority Sales,Customer Count\n2026-01-01,T001,100,20,30,2\n"
        rows = parse_sales_csv(text)
        self.assertEqual(rows[0]["Branch"], "T001")

    def test_temporary_xlsx_sheet_generation(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "fixture.xlsx"
            write_test_workbook(path)
            with zipfile.ZipFile(path) as archive:
                workbook = archive.read("xl/workbook.xml").decode()
            self.assertIn('name="INDEX"', workbook)
            self.assertIn('name="Analysis"', workbook)


if __name__ == "__main__":
    unittest.main()
