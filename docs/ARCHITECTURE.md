# Architecture

## Overview

The application is a local-first analytical system with a deliberately inspectable data flow:

```text
Runtime-selected CSV/XLSX files
      ↓
Local file parsing
      ↓
Normalization to typed JavaScript records
      ↓
Data-quality evaluation
      ↓
Central application state
      ↓
Global filters + analytical scope
      ↓
Reusable calculation functions
      ↓
KPIs / charts / tables / insights
      ↓
Cross-filter interactions
      ↓
Multi-sheet XLSX export
```

The central design principle is **Chart ≠ Data Source**. Visuals do not own business logic. Data is normalized first, calculations are performed centrally, and multiple presentation components consume the same analytical results.

## Layers

### Data layer

- Branch Master: branch attributes and lifecycle dates.
- Sales Collection: daily branch-level fact input.
- Budget Breakdown: monthly branch-level targets.
- Delivery Channel: optional embedded-component input.

### State layer

The central `state` object in the generalized V12 source stores loaded model data, current page, active filters, LFL scopes, and chart selections.

### Filter layer

The effective context combines date range, city, branch, lifecycle attributes, segment controls, and LFL scope. Cascading behavior prevents irrelevant selections.

### Calculation layer

Reusable functions calculate weighted AST, prorated budgets, budget achievement, branch performance, LFL, intervention momentum, Recovery scenarios, and Delivery contribution.

### Presentation layer

Responsive HTML/CSS and Chart.js consume centrally calculated results.

### Export layer

Current-page and complete analysis can be exported as styled multi-sheet XLSX workbooks with an INDEX sheet.

### Desktop layer

The `src-tauri/` folder packages the generated offline frontend using Tauri 2, Rust/Wry, WebView2, Windows x64, and NSIS configuration.

## Publication boundary

The repository contains the analytical architecture and source code but no committed business input dataset or business-result screenshot.
