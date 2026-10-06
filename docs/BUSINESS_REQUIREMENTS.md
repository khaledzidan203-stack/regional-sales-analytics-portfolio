# Business Requirements

## Business problem

A multi-branch retail operator needs one analytical view to understand sales performance against plan, distinguish traffic problems from basket-size problems, compare Like-for-Like performance, evaluate Pre/Post momentum without claiming causality, quantify an embedded Delivery component without double counting, and surface data-quality concerns before decisions are made.

## Functional requirements

1. Load privately held daily sales, monthly targets, branch master, and optional Delivery inputs at runtime.
2. Filter analysis by date, city, branch, lifecycle attributes, category, and size.
3. Prorate monthly budgets when the selected period covers only part of a month.
4. Calculate Total Sales, Core Retail, Service Channel, Priority Sales, Customer Count, and weighted AST.
5. Compare current results with the same calendar period one year earlier.
6. Support Strict Comparable and Total Region / Current Filters LFL modes.
7. Evaluate user-selected Pre/Post windows using scenario-based Recovery measures.
8. Treat Delivery as a component of Core Retail rather than incremental revenue.
9. Analyze Customer Count and AST jointly.
10. Detect and list common data-quality issues.
11. Support chart-driven cross-filtering.
12. Export the current page or complete analysis as a multi-sheet XLSX workbook.
13. Generate generalized action-review fields from current filtered findings.

## Non-functional requirements

- Local-first execution.
- No credentials or external database required.
- No real, synthetic, dummy, or generated business dataset committed.
- Clear metric definitions and reproducible formulas.
- Responsive desktop-oriented layout.
- Reproducible generation of the offline frontend.
- Offline desktop dependencies stored locally.
- No causal-impact claim from Recovery scenario estimates.
