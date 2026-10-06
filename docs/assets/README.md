# Presentation Assets

This directory contains presentation-only visual assets for the Regional Sales Performance Analytics project.

## Intended use

The primary overview image stored here is used by the repository README to summarize the analytical and desktop architecture at a glance.

Recommended filename:

`regional_sales_performance_analytics_overview.png`

The overview should represent only repository-supported claims, including:

- data-free public analytical architecture;
- 18-page regional sales performance engine;
- Total Sales, Budget, Achievement, Gap, Core Retail, Service Channel, Priority Sales, Customer Count, and weighted AST;
- same-period-last-year / Like-for-Like analysis;
- Strict Comparable versus Total Region scopes;
- Pre/Post Recovery scenario analysis;
- Expected Post and Estimated Recovery as non-causal scenario measures;
- Delivery Channel contribution without double counting;
- branch lifecycle analysis for openings and closures;
- Action Plan generation;
- Data Quality review;
- global multi-select filters and chart cross-filtering;
- current-page and full-analysis XLSX export;
- generalized HTML/CSS/JavaScript analytical source;
- Chart.js 4.4.1, chartjs-plugin-datalabels 2.2.0, and xlsx-js-style 1.2.0;
- reproducible generation of the offline frontend;
- Tauri 2 / Rust / Wry / WebView2 Windows desktop packaging;
- NSIS x64 release target;
- engine-neutral analytical SQL reference;
- Power BI mapping/design documentation only;
- automated validation, privacy scanning, and source/app parity checks.

## Evidence boundary

Assets in this directory are presentation summaries only. They are not business data, analytical result screenshots, Power BI runtime evidence, compiled desktop evidence, or proof of any real regional sales figures.

The repository is intentionally data-free. No real, synthetic, dummy, or generated business dataset is committed.

Authoritative claims remain defined by the generalized analytical source, generated offline frontend, generation manifest, Rust/Tauri source, tests, SQL references, KPI/methodology documentation, publication controls, and GitHub Actions validation.

Any visual KPI cards or charts in the overview must use neutral placeholders or abstract indicators rather than fabricated business figures.
