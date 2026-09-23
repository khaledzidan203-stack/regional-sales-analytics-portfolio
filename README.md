# Regional Sales Performance Analytics & Windows Desktop Application

A production-style regional sales performance and decision-support application combining an 18-page analytical engine with a Windows desktop delivery layer built with HTML, CSS, JavaScript, Chart.js, XLSX processing, Tauri 2, Rust, Wry, and WebView2.

This public portfolio repository contains the analytical architecture, desktop application source, methodology, tests, and documentation only. Business datasets are intentionally excluded.

No company data, customer data, branch performance data, credentials, or proprietary datasets are included. Analytical screenshots, executables, and installers are also excluded.

## Featured Portfolio

**Khaled Zidan — Healthcare & Business Data Analytics**

[Saudi Healthcare Analytics](https://github.com/khaledzidan203-stack/saudi-healthcare-analytics) ·
[Hospital360](https://github.com/khaledzidan203-stack/Hospital360) ·
[Online Retail Growth & Customer Intelligence](https://github.com/khaledzidan203-stack/online-retail-growth-customer-intelligence) ·
[Pharmacy Category Management](https://github.com/khaledzidan203-stack/pharmacy-category-management) ·
[Regional Sales Performance](https://github.com/khaledzidan203-stack/regional-sales-analytics-portfolio)

**Core stack:** Power BI · SQL · Python · DAX · Analytics Engineering · Healthcare / Pharmacy / Retail Analytics

## Executive Summary

The project centralizes multi-source performance logic in a local-first analytical application. It evaluates sales against budget, customer traffic and weighted average sales per transaction (AST), like-for-like performance, intervention recovery scenarios, component-channel contribution, branch lifecycle effects, and data readiness.

## Business Problem

Regional leadership needs a consistent way to identify budget gaps, distinguish traffic from basket-size effects, compare a stable branch base with prior-year periods, assess post-intervention momentum without claiming causality, isolate an embedded delivery component without double counting, and surface data issues before decisions are made.

## Project Objectives

- Maintain one calculation model across KPIs, charts, tables, insights, and exports.
- Support strict-comparable and total-region perspectives.
- Package the same analytical frontend as an offline Windows desktop application.
- Demonstrate the system without distributing business datasets.

## Final Product Overview

The portfolio source retains the final 18-page architecture, generalized as Branch, Core Retail, Service Channel, Delivery Channel, and Priority Sales. Users provide their own schema-compatible files at runtime; the repository ships no business data.

## Technology Stack

| Layer | Technology |
|---|---|
| Analytical UI | HTML5, CSS3, JavaScript |
| Visualization | Chart.js 4.4.1, chartjs-plugin-datalabels 2.2.0 |
| Spreadsheet input/export | xlsx-js-style 1.2.0 |
| Desktop | Tauri 2.11.5, Rust 2021, Wry, WebView2 |
| Windows packaging | NSIS, x64 |
| Validation | Python standard library, Node.js, GitHub Actions |

## Analytical Architecture

`Inputs -> parsing -> normalization -> data quality -> analytical state -> filters -> KPI engines -> charts/tables -> insights -> XLSX export`

See [analytical architecture](docs/architecture/analytical-architecture.md) and [data flow](docs/architecture/data-flow.md).

## Desktop Architecture

`Generalized V12 source -> prepare-app -> offline app/index.html -> Tauri -> Rust/Wry -> WebView2 -> Windows app -> NSIS installer`

See [desktop architecture](docs/architecture/desktop-architecture.md) and [release policy](docs/desktop_application/RELEASE_POLICY.md).

## Input Data

The runtime supports a Sales Collection CSV, Sales Budget Breakdown XLSX, and optional Delivery Channel XLSX. Schemas and grains are documented, but input files are not distributed.

## 18 Analytical Pages

The pages cover Executive Overview, Budget Gap, five LFL views, Recovery, Delivery impact, channel analyses, Customer Count and AST, geography and branch detail, segmentation, lifecycle, Action Plan, and Data Quality. See the [page catalog](docs/analytical_methodology/page-catalog.md).

## KPI Framework

Confirmed measures include Total Sales, Budget, Achievement, Gap, Core Retail, Service Channel, Priority Sales, Customer Count, weighted AST, mixes, LFL growth, recovery scenario measures, Delivery contribution, and Data Readiness. See the [KPI dictionary](docs/kpi_dictionary/KPI_DICTIONARY.md).

## Budget Analysis

Budget is evaluated at total and segment levels. Partial-month selections prorate monthly targets by selected calendar days before achievement and gap are calculated.

## LFL Framework

Current dates align with the same calendar dates in the prior year. Daily, weekly, monthly, cumulative, and branch-level views use the same central calculation path. See [LFL methodology](docs/lfl/methodology.md).

## Strict Comparable vs Total Region

Strict Comparable removes lifecycle distortion by requiring branch availability across both windows. Total Region follows current filters and includes network change. See [scope methodology](docs/lfl/strict-vs-total.md).

## Sales, Core Retail, Service Channel, Customer Count & AST LFL

Each major measure supports selectable strict or total scope with aligned current/prior periods and branch contribution analysis.

## Recovery & Intervention

User-selected Pre and Post windows calculate Pre LFL, Post LFL, momentum, shortfall movement, expected post, and estimated recovery. This is a counterfactual scenario, not causal proof. See [Recovery methodology](docs/recovery/methodology.md).

## Delivery Channel Impact

Delivery Channel is already included in Core Retail. It is never added again to Total Sales. The application evaluates Core Retail ex-Delivery, penetration, LFL uplift, budget uplift, and gap recovery. See [Delivery methodology](docs/delivery_channel/methodology.md).

## Customer Count & AST

AST is weighted: total sales divided by total customer count. Traffic and basket movement are analyzed together to distinguish volume and productivity effects.

## City / Branch / Category Analysis

Performance can be grouped by geography, branch, category, and size while retaining the active date, lifecycle, and chart-filter context.

## Lifecycle Analysis

New-branch ramp-up, closed-branch review, sales after closure, and budget after closure are separated from stable comparable performance.

## Action Plan Generator

The engine converts current filtered findings into generalized issue, evidence, branch scope, hypothesis, action, owner role, timing, and impact fields. Organization-specific owners and thresholds are excluded.

## Data Quality

The review layer checks malformed data, duplicates, missing mappings, lifecycle conflicts, invalid channel relationships, customer-count exceptions, incomplete periods, and Delivery matching. See [Data Quality rules](docs/data_quality/rules.md).

## Global Filtering and Chart Cross-filtering

Searchable multi-select slicers cover year, month, week, city, branch, status, category, and size. Date ranges and Delivery-branch scope are also supported. Chart clicks create visible filter chips with targeted clear controls. See [filtering documentation](docs/analytical_methodology/filtering-and-crossfiltering.md).

## Excel Export

Current-page and complete-analysis exports produce styled multi-sheet XLSX workbooks with an INDEX sheet. Full analysis can use current filters or the complete loaded model. See [XLSX export](docs/export/xlsx-export.md).

## Desktop Packaging

Version 1.0.2 uses Tauri 2, a hidden release console, disabled devtools, maximized startup, local JavaScript dependencies, WebView2 rendering, Windows x64 targeting, and NSIS packaging.

## Business Data Policy

No real, synthetic, dummy, or generated business dataset is committed. Formula tests use small in-memory fixtures or temporary files removed by the test process.

## Screenshots

Analytical screenshots are intentionally excluded from this public portfolio release.

## Repository Structure

`source/` holds the generalized single-file analytical source; `app/` is the reproducible offline frontend; `src-tauri/` contains desktop packaging; `docs/`, `sql/`, `tests/`, and `tools/` cover methodology and validation.

## Installation

Prerequisites: Node.js, Rust with the Windows MSVC toolchain, Tauri prerequisites, and WebView2. Run `npm ci`, `npm run prepare-app`, and `npm run desktop:build`. Building is optional for source review and produces local artifacts excluded by `.gitignore`.

## Usage

Open the generalized source or generated desktop frontend, upload privately held schema-compatible inputs at runtime, apply filters, inspect pages, and export the required analysis. Input data remains local to the running application.

## Validation

Run `npm test` and `npm run validate`. CI checks page count, versions, formulas, generated-source parity, forbidden artifacts, private paths, business-data files, and Markdown links.

## Privacy & Publication Safety

Publication controls are defined in [the allowlist](PUBLICATION_ALLOWLIST.md), [denylist](PUBLICATION_DENYLIST.md), and [sanitization manifest](SANITIZATION_MANIFEST.md). Existing private binaries are not approved for release.

## Limitations

No datasets, analytical screenshots, PBIX file, executable, or installer are distributed. Runtime conclusions depend on the completeness and correctness of user-supplied data. Recovery estimates do not prove causality.

## Lessons Learned

Central calculations, weighted ratios, explicit comparison scope, component-channel accounting, reproducible frontend generation, local dependency vendoring, and publication-first validation materially improve reliability. See [project lessons](docs/lessons_learned/project-lessons.md) and [technical decisions](docs/technical_decisions/).
