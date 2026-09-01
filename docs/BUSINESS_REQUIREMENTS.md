# Business Requirements

## Business problem

A multi-branch retail operator needs a single analytical view to understand sales performance against plan, distinguish traffic problems from basket-size problems, compare like-for-like performance, assess whether performance improved after an intervention, quantify the contribution of a delivery sub-channel without double counting, and surface data-quality concerns before decisions are made.

## Functional requirements

1. Load privately held daily sales, monthly targets, branch master, and optional delivery-channel inputs at runtime.
2. Filter analysis by date, city, and branch.
3. Prorate monthly budgets when the selected period covers only part of a month.
4. Calculate total, core-retail, service-channel, priority-sales, customer-count, and AST KPIs.
5. Compare current sales with the same calendar period one year earlier.
6. Support a strict comparable-branch LFL mode and a total-current-scope mode.
7. Evaluate pre/post intervention momentum using user-selectable intervention date.
8. Treat the delivery channel as a component of core retail rather than incremental revenue.
9. Classify branch performance using customer-count and AST behavior.
10. Detect and list common data-quality issues.
11. Provide cross-filtering from selected charts.
12. Export the current page or complete analysis as multi-sheet XLSX.

## Non-functional requirements

- Local-first and easy to run.
- No credentials or external database required.
- No real, synthetic, dummy, or generated business dataset committed to the repository.
- Clear metric definitions and reproducible formulas.
- Responsive layout suitable for desktop portfolio review.
- No claim of causal impact from counterfactual intervention estimates.
