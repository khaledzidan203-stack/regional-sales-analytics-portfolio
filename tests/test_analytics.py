import tempfile
import unittest
import zipfile
from datetime import date
from pathlib import Path

from tools.analytics_core import (
    budget_gap,
    core_retail_ex_delivery,
    estimated_recovery,
    expected_post,
    is_strict_comparable,
    lfl_growth,
    parse_sales_csv,
    prorated_budget,
    safe_div,
    total_sales,
    weighted_ast,
    write_test_workbook,
)


class AnalyticsTests(unittest.TestCase):
    def test_total_sales_and_delivery_non_double_counting(self):
        core = 100
        service = 20
        delivery = 10

        recorded_total = total_sales(core, service)

        self.assertEqual(recorded_total, 120)
        self.assertEqual(core_retail_ex_delivery(core, delivery), 90)
        self.assertEqual(core_retail_ex_delivery(core, delivery) + delivery, core)

        # Delivery is already embedded in Core Retail and must not be added again.
        self.assertNotEqual(recorded_total, core + service + delivery)

    def test_weighted_ast_uses_total_sales_over_total_customers(self):
        branch_sales = [100, 900]
        branch_customers = [1, 9]

        result = weighted_ast(sum(branch_sales), sum(branch_customers))

        self.assertEqual(result, 100)
        arithmetic_mean_of_branch_ast = ((100 / 1) + (900 / 9)) / 2
        self.assertEqual(arithmetic_mean_of_branch_ast, 100)

        # Unequal branch ASTs make the distinction visible.
        branch_sales = [100, 900]
        branch_customers = [1, 3]
        weighted = weighted_ast(sum(branch_sales), sum(branch_customers))
        naive = ((100 / 1) + (900 / 3)) / 2

        self.assertEqual(weighted, 250)
        self.assertEqual(naive, 200)
        self.assertNotEqual(weighted, naive)

    def test_zero_denominator_rules_return_none(self):
        self.assertIsNone(safe_div(10, 0))
        self.assertIsNone(weighted_ast(100, 0))
        self.assertIsNone(lfl_growth(100, 0))

    def test_budget_gap(self):
        self.assertEqual(budget_gap(900, 1000), -100)
        self.assertEqual(budget_gap(1100, 1000), 100)

    def test_partial_month_budget_proration(self):
        self.assertEqual(prorated_budget(31000, 31, 31), 31000)
        self.assertEqual(prorated_budget(31000, 15, 31), 15000)
        self.assertEqual(prorated_budget(29000, 14, 29), 14000)

        with self.assertRaises(ValueError):
            prorated_budget(31000, 32, 31)
        with self.assertRaises(ValueError):
            prorated_budget(31000, -1, 31)
        with self.assertRaises(ValueError):
            prorated_budget(31000, 1, 0)

    def test_lfl_alignment_formula(self):
        self.assertAlmostEqual(lfl_growth(120, 100), 0.20)
        self.assertAlmostEqual(lfl_growth(80, 100), -0.20)

    def test_strict_comparable_exclusions_and_boundaries(self):
        windows = [
            (date(2025, 1, 1), date(2025, 1, 31)),
            (date(2026, 1, 1), date(2026, 1, 31)),
        ]

        self.assertTrue(is_strict_comparable(date(2024, 1, 1), None, windows))
        self.assertFalse(is_strict_comparable(date(2025, 6, 1), None, windows))
        self.assertFalse(
            is_strict_comparable(
                date(2024, 1, 1),
                date(2025, 12, 31),
                windows,
            )
        )

        # Opening exactly on the earliest comparison start and closing exactly
        # on the latest comparison end are valid boundary cases.
        self.assertTrue(
            is_strict_comparable(
                date(2025, 1, 1),
                date(2026, 1, 31),
                windows,
            )
        )

    def test_recovery_scenario_negative_pre_trend(self):
        expected = expected_post(1000, -0.20)
        self.assertEqual(expected, 800)
        self.assertEqual(estimated_recovery(900, expected), 100)

    def test_recovery_scenario_positive_pre_trend(self):
        expected = expected_post(1000, 0.10)
        self.assertAlmostEqual(expected, 1100)
        self.assertEqual(estimated_recovery(1050, expected), -50)

    def test_priority_quality_rule_fixture(self):
        row = {"Core Retail Sales": 100, "Priority Sales": 110}
        self.assertGreater(row["Priority Sales"], row["Core Retail Sales"])

    def test_temporary_csv_parsing(self):
        text = (
            "Date,Branch,Core Retail Sales,Service Channel Sales,Priority Sales,Customer Count\n"
            "2026-01-01,T001,100,20,30,2\n"
        )
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
