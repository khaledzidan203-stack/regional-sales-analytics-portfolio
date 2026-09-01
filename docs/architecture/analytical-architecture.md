# Analytical Architecture

The application is a local-first, single-page analytical engine. Visual components consume centrally calculated results; charts are never treated as data sources.

```text
Input files
  -> parsing and schema recognition
  -> normalization to typed records
  -> data-quality evaluation
  -> central analytical state
  -> global and chart filters
  -> KPI, LFL, recovery, and channel engines
  -> charts, tables, and generated insights
  -> current-page or complete XLSX export
```

The same state and calculation functions drive every presentation and export path. This reduces discrepancies between headline KPIs, detail tables, charts, and downloaded workbooks.

The public source uses generalized business labels. It contains no embedded business records; inputs are selected locally at runtime.
