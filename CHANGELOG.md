# Changelog

## 1.0.2 — Current public source release

### Analytical hardening

- Retains the generalized 18-page analytical architecture.
- Adds stronger regression coverage for weighted AST, safe division, partial-month budget proration, strict comparable boundaries, recovery scenarios and embedded Delivery accounting.
- Clarifies the distinction between Strict Comparable and Total Region analysis.
- Preserves non-causal interpretation of Recovery scenario measures.

### Engineering hardening

- Retains reproducible offline frontend generation.
- Verifies source/app SHA-256 parity through the generation manifest.
- Keeps Chart.js, chartjs-plugin-datalabels and xlsx-js-style local in the generated desktop frontend.
- Clarifies Tauri Rust crate, CLI and build-tool versions separately.
- Clarifies that Windows packaging source is committed while NSIS binaries are not built or published by the current CI workflow.

### Presentation and governance

- Rebuilds public documentation around the independent analytical system rather than recruitment-oriented presentation.
- Adds project index, case study, technical walkthrough, evidence map, environment baseline and final validation documentation.
- Adds a reviewed abstract overview image under `docs/assets/`.
- Preserves the data-free publication policy: no real, synthetic, dummy or generated business dataset is committed.
- Preserves result-screenshot, binary, credential and private-infrastructure exclusions.
- Clarifies SQL as an engine-neutral analytical reference.
- Clarifies Power BI as design/mapping documentation only.

## 1.0.0 — 2026-08-26

### Added

- Executive Overview, Budget Gap, LFL, Intervention Impact, Delivery Channel Impact, Customer Count & AST, Branch Detail and Data Quality analysis.
- Cross-filtering by city and branch.
- Strict comparable versus total-scope LFL.
- Partial-month budget proration.
- Counterfactual intervention-recovery analysis with non-causal labeling.
- SQL examples, KPI catalog, architecture, data model and Power BI mapping.
- Optional Tauri desktop packaging structure.

### Security

- Removed private datasets, real geographic labels, real branch identifiers, organization branding, credentials and internal infrastructure details.
- Generalized business channel names and operating rules.
