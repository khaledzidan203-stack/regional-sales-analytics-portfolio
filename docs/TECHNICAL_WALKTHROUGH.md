# Technical Walkthrough — 60–90 Seconds

**0–10 seconds — Scope**

This is an 18-page regional sales decision-support system with a reproducible offline frontend and Tauri/Rust Windows desktop packaging source.

**10–25 seconds — Analytical model**

The central state combines branch master, daily sales, monthly budget and optional Delivery data. Total Sales, weighted AST, budget variance, LFL, recovery scenarios and lifecycle analysis all use shared calculation paths.

**25–40 seconds — Comparable performance**

Like-for-Like aligns current dates to the same calendar dates in the prior year. Strict Comparable removes branches that do not exist across both windows, while Total Region keeps network change visible.

**40–55 seconds — Scenario and channel logic**

Recovery compares Pre and Post LFL and calculates Expected Post plus Estimated Recovery without claiming causality. Delivery is treated as a component of Core Retail and is never added again to Total Sales.

**55–70 seconds — Interaction and export**

Searchable multi-select filters and chart cross-filtering operate on the same state used by KPI cards, tables and generated insights. Current-page and complete-analysis exports produce multi-sheet XLSX workbooks with an INDEX sheet.

**70–80 seconds — Reproducibility**

`prepare_app.mjs` generates the offline frontend from the generalized source, localizes required dependencies and records source/app SHA-256 hashes in a generation manifest.

**80–90 seconds — Boundaries**

The repository is data-free. SQL is an engine-neutral reference, Power BI is design/mapping documentation only, and compiled Windows binaries are intentionally excluded.
