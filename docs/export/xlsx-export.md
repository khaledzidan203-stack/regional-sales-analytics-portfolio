# XLSX Export

The final engine supports two commands:

- **Export Current Page**: exports the analytical sections associated with the active page.
- **Export All Analysis**: exports outputs across all 18 pages.

Complete analysis can use either the **Current Filtered View** or **Full Analysis** scope. Workbooks contain a styled `INDEX` worksheet followed by page-specific sheets. The index records page, section, scope, row count, and active filter context.

Exports preserve numeric cells, percentage/currency formats, wrapped headers, borders, column widths, frozen panes, autofilters, and page-specific tables. LFL, Recovery, Delivery, lifecycle, and Data Quality outputs use dedicated sheet specifications.

The final architecture is multi-sheet XLSX, not CSV-only. No exported workbook is committed to this repository.
