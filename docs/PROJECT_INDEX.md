# Project Index

## Start here

| Need | Document |
|---|---|
| Project overview | [Repository README](../README.md) |
| Case study | [CASE_STUDY.md](CASE_STUDY.md) |
| 60–90 second technical explanation | [TECHNICAL_WALKTHROUGH.md](TECHNICAL_WALKTHROUGH.md) |
| Evidence behind claims | [PROJECT_EVIDENCE_MAP.md](PROJECT_EVIDENCE_MAP.md) |
| Final validation boundary | [FINAL_RELEASE_VALIDATION.md](FINAL_RELEASE_VALIDATION.md) |

## Analytical design

- [18-Page Catalog](analytical_methodology/page-catalog.md)
- [KPI Dictionary](kpi_dictionary/KPI_DICTIONARY.md)
- [Filtering and Cross-Filtering](analytical_methodology/filtering-and-crossfiltering.md)
- [LFL Methodology](lfl/methodology.md)
- [Strict vs Total Scope](lfl/strict-vs-total.md)
- [Recovery Methodology](recovery/methodology.md)
- [Delivery Contribution](delivery_channel/methodology.md)
- [Data Quality](data_quality/rules.md)

## Engineering architecture

- [Analytical Architecture](architecture/analytical-architecture.md)
- [Data Flow](architecture/data-flow.md)
- [Desktop Architecture](architecture/desktop-architecture.md)
- [Desktop Version Baseline](desktop_application/VERSION_BASELINE.md)
- [Desktop Release Policy](desktop_application/RELEASE_POLICY.md)
- [XLSX Export](export/xlsx-export.md)

## Implementation artifacts

- `../source/Regional_Sales_Performance_V12_PORTFOLIO.html` — generalized 18-page source
- `../app/index.html` — generated offline frontend
- `../app/generation-manifest.json` — source/app SHA-256 parity contract
- `../app/vendor/` — local browser dependencies for offline desktop use
- `../src-tauri/` — desktop packaging source
- `../tools/` — analytical helpers and validation
- `../tests/` — formula/source/publication tests
- `../sql/` — engine-neutral analytical SQL references

## Publication governance

- [Publication Allowlist](../PUBLICATION_ALLOWLIST.md)
- [Publication Denylist](../PUBLICATION_DENYLIST.md)
- [Sanitization Manifest](../SANITIZATION_MANIFEST.md)
- [Privacy and Sanitization](PRIVACY_AND_SANITIZATION.md)

No committed business dataset or analytical result screenshot is required for this release.
