# Architecture

## Overview

The public portfolio version is a local-first analytical application. It intentionally keeps the data flow simple and inspectable:

```text
Runtime-selected CSV/XLSX files
      ↓
Local file parsing
      ↓
Normalization to typed JavaScript records
      ↓
Central application state
      ↓
Global filters + analytical scope
      ↓
Reusable calculation functions
      ↓
KPIs / charts / tables
      ↓
Cross-filter interactions
      ↓
Multi-sheet XLSX export
```

The central design principle is **Chart ≠ Data Source**. Visuals do not own business logic. Data is normalized first, calculations are performed centrally, and multiple visual components consume the same analytical results.

## Layers

### Data layer
- Branch Master: branch attributes and lifecycle dates inside the Budget workbook.
- Sales Collection: daily branch-level fact input.
- Budget Breakdown: monthly branch-level targets.
- Delivery Channel: optional embedded-component input.

### State layer
The central `state` object in the generalized V12 source stores loaded model data, current page, active filters, LFL scopes, and chart selections.

### Filter layer
The effective context combines date range, city, branch, and LFL scope. City-to-branch cascading behavior prevents irrelevant branch selections.

### Calculation layer
Reusable functions calculate weighted AST, prorated budgets, budget achievement, branch performance, LFL, intervention momentum, and delivery-channel contribution.

### Presentation layer
The application uses responsive HTML/CSS and Chart.js. Declared chart mappings update analytical filters.

### Export layer
Current-page and complete analysis can be exported as styled multi-sheet XLSX workbooks with an INDEX sheet.

## Desktop layer
The `src-tauri/` folder packages the generated offline frontend using Tauri 2, Rust/Wry, WebView2, Windows x64, and NSIS configuration.
