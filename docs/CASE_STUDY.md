# Case Study — Regional Sales Performance Intelligence

## Context

Regional performance analysis becomes unreliable when budget, traffic, basket value, comparable-base movement, lifecycle change and channel contribution are calculated independently.

This project centralizes those definitions into one local-first analytical engine and packages the same generated frontend for Windows desktop delivery.

## Business questions

The system is designed to answer:

1. Where is the budget shortfall concentrated?
2. Is performance change driven by traffic, AST, or both?
3. Is the comparable branch base improving year over year?
4. How do openings and closures change the total-region view?
5. Did performance momentum improve across selected Pre/Post windows?
6. What does an embedded Delivery component contribute without double counting?
7. Which current findings should enter an action-review workflow?
8. Are the loaded files complete and logically consistent enough for interpretation?

## Analytical architecture

The engine follows:

`Input → Parse → Normalize → DQ → Central State → Filters → KPI Engines → Visuals/Tables → Insights → XLSX Export`

Charts are presentation consumers. Central calculations remain the source of truth.

## Weighted AST

AST is calculated as:

`Total Sales / Total Customer Count`

This avoids the bias created by averaging branch-level or day-level AST values with unequal transaction counts.

## Budget analysis

Monthly targets can be prorated when the active date filter includes only part of a month. This avoids comparing partial actuals with a full-month target.

## Like-for-Like

The system provides two valid perspectives:

- **Strict Comparable** — only branches that exist across both comparison windows.
- **Total Region / Current Filters** — the selected network including lifecycle change.

The distinction separates stable-base performance from network expansion or closure effects.

## Recovery scenario

Pre and Post windows calculate:

- Pre LFL
- Post LFL
- momentum
- Expected Post
- Estimated Recovery

Expected Post is a continuation scenario based on the Pre trend. Estimated Recovery measures deviation from that scenario.

It is useful for structured review but is not causal proof.

## Delivery accounting

Delivery is already embedded in Core Retail.

Therefore:

`Total Sales = Core Retail + Service Channel`

and:

`Core Retail ex-Delivery = Core Retail - Delivery`

This protects total sales from double counting.

## Lifecycle analysis

Opening and closing dates are used for:

- comparable-base eligibility;
- ramp-up review;
- closure review;
- post-closure sales checks;
- post-closure budget checks.

## Delivery

The analytical source is generalized and data-free.

The generated offline frontend replaces required CDN dependencies with local vendor files and is hosted through Tauri/Rust for Windows desktop packaging.

## Publication model

The public project intentionally commits no business dataset and no result screenshot with business figures.

Tests use in-memory objects and temporary files, allowing formulas, source structure, exports, and publication controls to be validated without exposing or fabricating performance data.
