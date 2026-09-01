# Data Flow

| Stage | Responsibility | Output |
|---|---|---|
| Input | Read Sales CSV, Budget XLSX, optional Delivery XLSX | Raw rows in browser memory |
| Parse | Identify sheets and accepted headers | JavaScript row objects |
| Normalize | Parse dates/numbers, group Date x Branch, attach master attributes | Typed facts and dimensions |
| Quality | Evaluate structural, lifecycle, mapping, and channel checks | Readiness score and review queue |
| State | Store normalized facts, active page, scope, and filters | One analytical context |
| Calculate | Aggregate KPIs, LFL, Recovery, lifecycle, and Delivery effects | Reusable result objects |
| Present | Render KPIs, charts, tables, and interpretations | Interactive analysis |
| Export | Recalculate requested scope and build styled worksheets | Multi-sheet XLSX workbook |

Uploaded records remain local to the running browser/WebView session. The repository contains no business data files.
