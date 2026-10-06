# Regional Sales Performance Analytics

## 18-Page Decision-Support Engine & Windows Desktop Architecture

[![Repository Validation](https://github.com/khaledzidan203-stack/regional-sales-analytics-portfolio/actions/workflows/validate.yml/badge.svg)](https://github.com/khaledzidan203-stack/regional-sales-analytics-portfolio/actions/workflows/validate.yml)

**Live data-free interface:** https://khaledzidan203-stack.github.io/regional-sales-analytics-portfolio/app/

Regional Sales Performance Analytics is a local-first analytical system for multi-branch performance management. It combines an 18-page HTML/CSS/JavaScript analytical engine with Chart.js visualization, XLSX input/export, reusable formula tests, publication controls, and a Tauri/Rust Windows desktop packaging layer.

> **Data-free boundary:** this repository intentionally commits no real, synthetic, dummy, or generated business dataset. Runtime results depend on user-supplied schema-compatible files selected locally. No company data, customer data, branch-performance records, credentials, compiled executable, installer, or analytical result screenshot is published.

<img src="docs/assets/Regional%20Sales%20Analytics%20Dashboard.png" alt="Regional Sales Performance Analytics overview" width="100%">

> **Visual evidence note:** the image above is a presentation schematic. Its charts and KPI cards use placeholders or illustrative shapes rather than committed business results. Authoritative evidence comes from the generalized analytical source, generated offline frontend, tests, manifest, desktop source, SQL references, methodology, and validation workflows.

**Start here:** [Case study](docs/CASE_STUDY.md) · [Technical walkthrough](docs/TECHNICAL_WALKTHROUGH.md) · [Evidence map](docs/PROJECT_EVIDENCE_MAP.md) · [Project index](docs/PROJECT_INDEX.md) · [Final validation](docs/FINAL_RELEASE_VALIDATION.md)

## Project at a glance

| Area | Current implementation |
|---|---|
| Analytical interface | 18 integrated pages |
| Frontend | HTML5, CSS3, JavaScript |
| Visualization | Chart.js 4.4.1 + chartjs-plugin-datalabels 2.2.0 |
| Spreadsheet processing | xlsx-js-style 1.2.0 |
| Generated offline frontend | `app/index.html` |
| Source-to-app traceability | SHA-256 generation manifest |
| Desktop host | Tauri/Rust/Wry/WebView2 architecture |
| Tauri Rust crate | 2.11.5 |
| Tauri CLI | 2.8.4 |
| Windows bundle target | NSIS, x64 |
| Formula tests | Python standard library |
| SQL | engine-neutral analytical reference |
| Power BI | design/mapping documentation only |
| Business datasets | intentionally excluded |
| Result screenshots | intentionally excluded |
| Validation | GitHub Actions + privacy/publication gates |

## Business problem

Regional leadership needs one consistent analytical model to answer several questions without allowing charts, exports, or pages to drift into different definitions:

- Where is the budget gap concentrated?
- Is weakness driven by traffic, basket value, or both?
- Is performance improving on a comparable branch base?
- How should openings and closures be separated from stable-base performance?
- Did Pre/Post performance momentum change after an intervention date?
- What does an embedded delivery component contribute without double counting?
- Which branches, cities, categories, or size groups require review?
- Are the loaded files ready for interpretation?
- Can the same filtered state be exported reliably?

The project centralizes those questions into one calculation and filter architecture.

## End-to-end architecture

```text
User-Supplied Local Files
        ↓
Parsing + Schema Recognition
        ↓
Typed Normalization
        ↓
Data Quality Evaluation
        ↓
Central Analytical State
        ↓
Global Filters + Chart Cross-Filters
        ↓
KPI / Budget / LFL / Recovery / Channel Engines
        ↓
Charts + Tables + Generated Insights
        ↓
Current-Page or Full XLSX Export
        ↓
Offline Frontend
        ↓
Tauri / Rust Windows Desktop Packaging
```

Visuals are consumers of centrally calculated results; they are not treated as independent data sources.

## Runtime input model

The analytical engine supports schema-compatible local inputs for:

- Sales Collection CSV;
- Sales Budget Breakdown XLSX;
- optional Delivery Channel XLSX.

The logical analytical model is:

```text
Branch Master (1) ─────< Daily Sales (*)
      │
      ├───────────────< Monthly Budget (*)
      │
      └───────────────< Delivery Channel (*)
```

Primary grains:

- Branch Master: one row per branch;
- Daily Sales: Date × Branch;
- Monthly Budget: Month × Branch;
- Delivery Channel: Date × Branch with channel activity.

No input files are committed.

## Core KPI framework

The confirmed model includes:

- Total Sales
- Core Retail Sales
- Service Channel Sales
- Priority Sales
- Customer Count
- weighted AST
- Budget
- Achievement
- Budget Gap
- segment achievement
- Priority Rate
- Service Mix
- LFL Growth
- Strict LFL
- Total LFL
- Pre LFL
- Post LFL
- Momentum
- Expected Post
- Estimated Recovery
- Delivery % of Core Retail
- Core Retail ex-Delivery

### Total Sales

```text
Total Sales = Core Retail Sales + Service Channel Sales
```

### Weighted AST

```text
AST = Total Sales / Total Customer Count
```

The engine does **not** average pre-calculated daily AST values.

### Budget Gap

```text
Budget Gap = Total Sales - Budget
```

Partial-month selections prorate monthly targets by the selected calendar days before achievement and gap are interpreted.

## Like-for-Like framework

Current dates are aligned with the same calendar dates in the prior year.

The system supports:

- daily LFL;
- cumulative LFL;
- weekly LFL;
- monthly LFL;
- branch-level contribution;
- multiple sales/customer measures.

### Strict Comparable

Strict scope removes lifecycle distortion by requiring a branch to exist across both comparison windows.

### Total Region / Current Filters

Total scope follows the current selected population without comparable-branch exclusion.

Keeping both views prevents network openings and closures from being mistaken for stable-base performance change.

## Traffic and AST analysis

Customer Count and weighted AST are analyzed together so the user can distinguish:

- lower traffic with stable basket value;
- stable traffic with lower basket value;
- improvement in both;
- offsetting movement between traffic and basket.

This prevents sales movement from being interpreted as one undifferentiated outcome.

## Recovery and intervention scenario

Users define Pre and Post windows.

The model calculates:

- Pre LFL;
- Post LFL;
- momentum in percentage points;
- Expected Post;
- Estimated Recovery.

```text
Expected Post = Post LY × (1 + Pre LFL)

Estimated Recovery = Actual Post - Expected Post
```

This is a **counterfactual scenario indicator**, not proof that an intervention caused the observed change.

## Embedded Delivery contribution

Delivery Channel is modeled as a component already contained within Core Retail.

Therefore:

```text
Total Sales = Core Retail + Service Channel
```

and **not**:

```text
Total Sales = Core Retail + Service Channel + Delivery
```

For contribution analysis:

```text
Core Retail ex-Delivery = Core Retail - Delivery
```

This prevents double counting.

## Branch lifecycle

Opening and closing dates support:

- comparable-base eligibility;
- new-branch ramp-up review;
- closed-branch review;
- sales-after-closure checks;
- budget-after-closure checks.

Lifecycle effects are separated from stable comparable performance.

## 18 analytical pages

| # | Page |
|---:|---|
| 1 | Executive Overview |
| 2 | Budget Gap |
| 3 | Sales Like-for-Like |
| 4 | Core Retail Like-for-Like |
| 5 | Service Channel Like-for-Like |
| 6 | Customer Count & AST Like-for-Like |
| 7 | Recovery & Intervention Impact |
| 8 | Delivery Channel Impact |
| 9 | Service Channel Analysis |
| 10 | Core Retail Analysis |
| 11 | Priority Sales Analysis |
| 12 | Customer Count & AST |
| 13 | City Performance |
| 14 | Branch Detail |
| 15 | Category & Size |
| 16 | New & Closed Branches |
| 17 | Action Plan Generator |
| 18 | Data Quality |

See the full [page catalog](docs/analytical_methodology/page-catalog.md).

## Filtering and cross-filtering

Searchable multi-select controls support:

- Year
- Month
- Week
- Date From / Date To
- City
- Branch
- Delivery-branch scope
- Status
- Category
- Size Group

Chart selections create visible filter chips with targeted clear controls.

The analytical state is shared so cards, charts, tables, insights, and exports operate under the same filter context.

## Action Plan Generator

The engine converts current filtered findings into generalized fields such as:

- issue;
- evidence;
- branch scope;
- hypothesis;
- suggested action;
- owner role;
- timing;
- expected impact.

Organization-specific owners and private thresholds are intentionally excluded.

## Data Quality layer

The review layer checks conditions such as:

- malformed rows;
- duplicates;
- missing branch mappings;
- lifecycle conflicts;
- invalid segment relationships;
- customer-count exceptions;
- incomplete periods;
- Delivery matching issues.

Data Quality is a decision-readiness layer rather than a hidden preprocessing step.

## XLSX export

The analytical source supports:

- Current Page export;
- Complete Analysis export;
- styled multi-sheet XLSX workbooks;
- INDEX sheet;
- current-filter or complete-model export scope.

The workbook structure is also exercised through temporary-file tests without committing business data.

## Source-to-app reproducibility

The generalized source is retained at:

`source/Regional_Sales_Performance_V12_PORTFOLIO.html`

The offline frontend is generated by:

`tools/prepare_app.mjs`

Generation performs:

- replacement of required CDN references with local vendor files;
- desktop safe-area injection;
- 18-page count extraction;
- SHA-256 source hash;
- SHA-256 generated-app hash;
- version capture.

The resulting contract is stored in:

`app/generation-manifest.json`

CI regenerates the app and requires zero diff against the committed generated frontend.

## Windows desktop architecture

The generated frontend is packaged through the Tauri source layer:

```text
Generalized V12 Source
        ↓
prepare_app.mjs
        ↓
Offline app/index.html
        ↓
Tauri CLI
        ↓
Rust / Wry Host
        ↓
WebView2
        ↓
Windows x64 Application
        ↓
NSIS Bundle Target
```

Current source configuration includes:

- application version 1.0.2;
- Tauri Rust crate 2.11.5;
- Tauri CLI 2.8.4;
- Tauri build dependency 2.6.3;
- Windows GUI subsystem;
- maximized startup;
- resizable window;
- devtools disabled;
- local-content CSP;
- NSIS target.

**Boundary:** GitHub Actions validates packaging source and generated frontend parity, but it does not build or publish an NSIS binary in this repository. Executables and installers remain excluded.

## Engine-neutral SQL reference

The `sql/` folder provides portable logical examples for:

- schema design;
- core KPIs;
- LFL analysis;
- data quality;
- recovery analysis;
- Delivery contribution.

The SQL is intentionally engine-neutral. Date syntax or parameter binding may require adjustment for a selected database engine.

## Power BI boundary

`docs/POWER_BI_MAPPING.md` maps the generalized model to a recommended star schema and DAX patterns.

There is **no committed PBIX, PBIP, PBIR, TMDL or PBIT runtime implementation**.

Power BI is therefore an implementation blueprint, not runtime evidence.

## Data-free publication model

The repository intentionally excludes:

- real business datasets;
- synthetic business datasets;
- dummy/generated business datasets;
- business CSV/XLSX inputs;
- customer or transaction records;
- real branch identifiers;
- company branding;
- result screenshots containing business figures;
- executables and installers;
- credentials and internal infrastructure details.

Tests use in-memory objects or temporary files that are removed automatically.

This design allows analytical formulas and architecture to be reviewed without exposing or fabricating operational results.

## Validation

Run:

```bash
npm ci
npm test
npm run validate
npm run prepare-app
git diff --exit-code -- app/index.html app/generation-manifest.json
```

GitHub Actions checks:

- 18-page source structure;
- version consistency;
- analytical formula tests;
- JavaScript syntax;
- local desktop dependencies;
- source/app SHA-256 manifest parity;
- forbidden artifacts;
- business-data exclusion;
- Markdown links;
- privacy-sensitive terminology;
- credentials, paths, networks, and branding patterns;
- generated frontend reproducibility.

## Repository structure

```text
source/                generalized 18-page analytical source
app/                   reproducibly generated offline frontend + local vendor files
src-tauri/             Tauri/Rust desktop packaging source
tools/                 analytical helpers, generator, validation, privacy scan
tests/                 formula, source, and publication-contract tests
sql/                   engine-neutral analytical SQL references
docs/                  methodology, architecture, KPI and evidence documentation
docs/assets/           presentation-only schematic assets
.github/workflows/     automated validation
```

## Documentation

- [Project Index](docs/PROJECT_INDEX.md)
- [Case Study](docs/CASE_STUDY.md)
- [Technical Walkthrough](docs/TECHNICAL_WALKTHROUGH.md)
- [Project Evidence Map](docs/PROJECT_EVIDENCE_MAP.md)
- [Architecture](docs/architecture/analytical-architecture.md)
- [Data Flow](docs/architecture/data-flow.md)
- [Desktop Architecture](docs/architecture/desktop-architecture.md)
- [KPI Dictionary](docs/kpi_dictionary/KPI_DICTIONARY.md)
- [LFL Methodology](docs/lfl/methodology.md)
- [Recovery Methodology](docs/recovery/methodology.md)
- [Delivery Methodology](docs/delivery_channel/methodology.md)
- [Data Quality Rules](docs/data_quality/rules.md)
- [XLSX Export](docs/export/xlsx-export.md)
- [Power BI Mapping](docs/POWER_BI_MAPPING.md)
- [Privacy and Sanitization](docs/PRIVACY_AND_SANITIZATION.md)
- [Final Release Validation](docs/FINAL_RELEASE_VALIDATION.md)

## Limitations

- No business dataset is distributed, so the public repository does not publish business KPI outcomes.
- Runtime conclusions depend on the completeness and correctness of locally supplied files.
- Recovery estimates are scenario measures, not causal proof.
- The SQL layer is a portable reference rather than a database-specific deployed implementation.
- Power BI is design-only.
- CI does not publish or prove an NSIS installation on a clean Windows machine.
- The hero graphic is a presentation schematic, not an analytical result screenshot.

Licensed under the [MIT License](LICENSE).
