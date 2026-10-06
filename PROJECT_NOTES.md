# Project Notes

## Purpose

Regional Sales Performance Analytics is a data-free analytical and desktop-application architecture for multi-branch performance management.

## Core design choices

1. **One analytical state** — KPI cards, charts, tables, insights and exports consume centrally calculated results.
2. **Weighted ratios** — AST is derived from total sales and total customers rather than averaging pre-calculated ratios.
3. **Explicit comparison scope** — Strict Comparable and Total Region answer different business questions.
4. **Lifecycle-aware LFL** — openings and closures are controlled before comparable-base interpretation.
5. **Scenario discipline** — Recovery metrics are counterfactual review measures and are not labeled as causal effects.
6. **Component accounting** — Delivery is embedded in Core Retail and is never added again to Total Sales.
7. **Data-free publication** — no real or fabricated business result dataset is committed.
8. **Reproducible frontend generation** — the offline app is generated from the generalized analytical source and validated by SHA-256 parity.
9. **Local desktop dependencies** — required browser libraries are vendored for the generated desktop frontend.
10. **Explicit runtime boundaries** — packaging source is committed, while compiled binaries and installers are excluded.

## Implemented layers

- 18-page analytical source;
- local file parsing and schema recognition;
- global filters and cross-filtering;
- KPI / budget / LFL / recovery / channel logic;
- Data Quality review;
- multi-sheet XLSX export;
- reproducibly generated offline frontend;
- Tauri/Rust desktop packaging source;
- engine-neutral SQL references;
- Power BI mapping documentation;
- automated formula, source, privacy and publication validation.

## Scaling path

A production implementation would normally add governed source connectors, business-owned threshold tables, refresh orchestration, centralized identity/authorization, monitored data-quality SLAs, deployment telemetry and environment-specific configuration outside the analytical source.
