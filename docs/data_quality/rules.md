# Data Quality Rules

| Check | Purpose |
|---|---|
| Blank or invalid rows | Detect records that cannot form a dated branch fact |
| Duplicate Date x Branch groups | Expose aggregation from multiple source rows |
| Missing/unmapped branches | Prevent silent loss of dimensional context |
| Activity before opening | Identify lifecycle conflicts |
| Activity after closing | Identify invalid post-close sales |
| Budget after closing | Identify target allocation after closure |
| Priority Sales > Core Retail | Detect an invalid subset relationship |
| Zero customer count with sales | Prevent misleading AST interpretation |
| Negative customer count | Flag logically invalid traffic |
| Incomplete current period | Warn against comparing partial and complete windows |
| Delivery without matching sales | Prevent unsupported contribution attribution |
| Delivery > Core Retail | Detect a broken embedded-component relationship |
| Missing branch mapping | Surface master-data coverage gaps |

Negative Service Channel sales may represent returns or reversals and are not automatically treated as errors. They remain visible for business review.
