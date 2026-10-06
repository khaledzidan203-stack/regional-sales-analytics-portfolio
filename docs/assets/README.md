# Presentation Assets

This directory contains presentation-only visual assets for Regional Sales Performance Analytics.

## Current overview

`Regional Sales Analytics Dashboard.png`

The root README uses this image as a high-level schematic of the analytical and desktop-delivery architecture.

## Evidence-supported scope

The repository supports:

- 18 analytical pages;
- Total Sales, Budget, Achievement, Gap, Core Retail, Service Channel, Priority Sales, Customer Count and weighted AST;
- Like-for-Like analysis;
- Strict Comparable and Total Region scopes;
- Pre/Post recovery scenario analysis;
- Expected Post and Estimated Recovery as non-causal scenario measures;
- embedded Delivery contribution without double counting;
- branch lifecycle analysis;
- Action Plan generation;
- Data Quality review;
- global filtering and chart cross-filtering;
- current-page and complete multi-sheet XLSX export;
- generalized HTML/CSS/JavaScript analytical source;
- Chart.js, chartjs-plugin-datalabels and xlsx-js-style;
- reproducible offline frontend generation;
- Tauri/Rust/Wry/WebView2 desktop packaging source;
- NSIS x64 bundle target;
- engine-neutral SQL references;
- Power BI mapping/design documentation;
- automated validation and privacy scanning.

## Evidence boundary

The overview image is a **presentation schematic**, not an analytical result screenshot.

Its cards, charts, region names, action rows, shapes and placeholder values are illustrative. They are not committed business data and do not prove any business outcome.

The repository is intentionally data-free. No real, synthetic, dummy or generated business dataset is committed.

Authoritative implementation evidence remains:

- `source/Regional_Sales_Performance_V12_PORTFOLIO.html`;
- `app/index.html`;
- `app/generation-manifest.json`;
- `src-tauri/`;
- `tools/`;
- `tests/`;
- `sql/`;
- analytical methodology and publication-governance documentation;
- GitHub Actions validation.

No Power BI runtime file, compiled Windows executable, installer or business-result screenshot is claimed.
