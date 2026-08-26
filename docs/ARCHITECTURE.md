# Architecture

## Overview

The public portfolio version is a local-first analytical application. It intentionally keeps the data flow simple and inspectable:

```text
Synthetic CSV files
      ↓
Browser fetch / CSV parsing
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
CSV export
```

The central design principle is **Chart ≠ Data Source**. Visuals do not own business logic. Data is normalized first, calculations are performed centrally, and multiple visual components consume the same analytical results.

## Layers

### Data layer
- `branch_master.csv`: branch attributes and lifecycle dates.
- `sales_daily.csv`: daily branch-level fact table.
- `monthly_budget.csv`: monthly branch-level targets.
- `delivery_channel.csv`: channel component fact table.

### State layer
`S` in `src/index.html` stores loaded model data, current page, active filters, LFL scope, and the active export table.

### Filter layer
The effective context combines date range, city, branch, and LFL scope. City-to-branch cascading behavior prevents irrelevant branch selections.

### Calculation layer
Reusable functions calculate weighted AST, prorated budgets, budget achievement, branch performance, LFL, intervention momentum, and delivery-channel contribution.

### Presentation layer
The application uses responsive HTML/CSS with lightweight SVG and DOM-based charts. Bar-chart selections can update global city or branch filters.

### Export layer
The visible analytical table can be exported as CSV. The private production project used a richer spreadsheet export engine; this public version intentionally keeps the distributable dependency footprint small.

## Optional desktop layer
The `src-tauri/` folder demonstrates how the same local frontend can be packaged as a Windows desktop application using Tauri 2. The browser version remains the easiest path for reviewers.
