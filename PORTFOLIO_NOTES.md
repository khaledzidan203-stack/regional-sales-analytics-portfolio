# Portfolio Notes

## What I personally built

I designed the analytical logic and end-to-end workflow behind this project: data ingestion, normalization, KPI definitions, business-rule validation, like-for-like analysis, budget comparison, intervention analysis, channel-contribution logic, data-quality review, interactive filtering, analytical tables, and desktop packaging. The public repository preserves generalized architecture and logic while excluding all business datasets.

## Analytical skills demonstrated

- Translating business questions into measurable KPIs.
- Building reusable calculation logic rather than chart-specific formulas.
- Weighted KPI calculation, especially AST.
- Partial-period target proration.
- Same-period-last-year and like-for-like analysis.
- Comparable-entity scope design to control for openings and closures.
- Pre/post intervention analysis and percentage-point momentum.
- Counterfactual scenario construction with appropriate non-causal interpretation.
- Component-vs-incremental sales modeling to prevent double counting.
- Traffic vs basket decomposition using Customer Count and AST.
- Data-quality controls for duplicates, missing master mappings, and logical inconsistencies.
- Interactive analytical UX and cross-filtering.
- Documentation of data model, formulas, and business requirements.

## Business problems solved

- Which branches are driving the budget gap?
- Is performance weakness caused more by traffic or basket size?
- Is the same comparable branch base improving or declining year over year?
- Did performance momentum improve after an intervention date?
- How much does a delivery sub-channel contribute without overstating total sales?
- Which data-quality issues should be reviewed before decisions are made?

## Technologies used

- HTML5 / CSS3 / JavaScript.
- Local-first browser analytics.
- CSV/XLSX runtime input architecture; no input files are distributed.
- SVG / DOM-based lightweight charts.
- Tauri 2 / Rust desktop packaging structure.
- SQL analytical query examples.
- Power BI / DAX mapping documentation.
- Git / GitHub repository practices.

## Interview discussion points

1. Explain why AST is calculated as total sales divided by total customers rather than the average of daily AST.
2. Explain how prorating monthly budget avoids unfair comparisons for partial-month filters.
3. Explain the difference between Total LFL and Strict Comparable LFL.
4. Explain how branch opening and closing dates affect comparable-store analysis.
5. Explain why the intervention-recovery estimate is useful but not causal proof.
6. Explain the double-counting risk when a delivery channel is already embedded inside a main sales segment.
7. Explain the separation between raw data, normalized model, filter context, calculation engine, and visualization.
8. Explain how the same model would be implemented in Power BI using a star schema and DAX.
9. Explain why Data Quality is a review layer rather than automatically blocking all analytics.
10. Explain how the public repository was sanitized for portfolio use without exposing private business data.
