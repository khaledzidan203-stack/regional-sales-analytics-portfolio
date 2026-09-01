"""Generalized analytical formulas used by data-free portfolio tests."""
from __future__ import annotations

import csv
import io
import zipfile
from datetime import date
from pathlib import Path


def safe_div(numerator: float, denominator: float):
    return numerator / denominator if denominator else None


def total_sales(core_retail: float, service_channel: float) -> float:
    return core_retail + service_channel


def weighted_ast(sales: float, customers: float):
    return safe_div(sales, customers)


def budget_gap(actual: float, budget: float) -> float:
    return actual - budget


def lfl_growth(current: float, previous: float):
    return safe_div(current - previous, previous)


def expected_post(post_ly: float, pre_lfl: float) -> float:
    return post_ly * (1 + pre_lfl)


def estimated_recovery(actual_post: float, expected: float) -> float:
    return actual_post - expected


def core_retail_ex_delivery(core_retail: float, delivery: float) -> float:
    return core_retail - delivery


def is_strict_comparable(opened: date | None, closed: date | None, windows) -> bool:
    return all((opened is None or opened <= start) and (closed is None or closed >= end) for start, end in windows)


def parse_sales_csv(text: str):
    rows = list(csv.DictReader(io.StringIO(text)))
    required = {"Date", "Branch", "Core Retail Sales", "Service Channel Sales", "Priority Sales", "Customer Count"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError("Sales fixture schema is invalid")
    return rows


def write_test_workbook(path: Path):
    """Write a minimal XLSX package for export-architecture tests only."""
    content_types = '<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/><Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>'
    root_rels = '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>'
    workbook = '<?xml version="1.0"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="INDEX" sheetId="1" r:id="rId1"/><sheet name="Analysis" sheetId="2" r:id="rId2"/></sheets></workbook>'
    workbook_rels = '<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/></Relationships>'
    sheet = '<?xml version="1.0"?><worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData/></worksheet>'
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("_rels/.rels", root_rels)
        archive.writestr("xl/workbook.xml", workbook)
        archive.writestr("xl/_rels/workbook.xml.rels", workbook_rels)
        archive.writestr("xl/worksheets/sheet1.xml", sheet)
        archive.writestr("xl/worksheets/sheet2.xml", sheet)
