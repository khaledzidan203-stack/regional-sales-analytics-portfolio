# Project Evidence Map

| Claim | Primary evidence | Evidence type |
|---|---|---|
| 18 analytical pages | source `PAGE_META`, validator, page catalog | Source + automated check |
| Weighted AST | `tools/analytics_core.py`, KPI dictionary, tests | Source + test |
| Budget gap logic | analytical helper + KPI dictionary | Source + test |
| LFL formula | helper + LFL documentation + tests | Source + test |
| Strict comparable logic | helper + strict-vs-total docs + tests | Source + test |
| Recovery scenario | helper + recovery methodology + tests | Source + test |
| Delivery non-double-counting | helper + Delivery methodology + tests | Source + test |
| Multi-sheet XLSX structure | source + temporary workbook test + export docs | Source + test |
| Searchable multi-select filters | generalized source + filtering docs | Source evidence |
| Chart cross-filtering | generalized source + filtering docs | Source evidence |
| Data Quality page | source + page catalog + DQ rules | Source + docs |
| Reproducible offline frontend | `prepare_app.mjs` + generation manifest + CI diff check | Automated contract |
| Local desktop dependencies | `app/vendor/` + validator | Source + automated check |
| Tauri/Rust Windows packaging | `src-tauri/` | Packaging source |
| NSIS source configuration | `src-tauri/tauri.conf.json` | Configuration evidence |
| Compiled installer in public release | none committed | **Not claimed** |
| Engine-neutral SQL layer | `sql/` | Reference implementation |
| Power BI runtime model | no PBIX/PBIP/PBIR/TMDL committed | **Not claimed** |
| Power BI mapping | `POWER_BI_MAPPING.md` | Blueprint |
| Business KPI results | no business dataset committed | **Not claimed** |
| Analytical result screenshots | intentionally excluded | **Not claimed** |
| Presentation overview | `assets/Regional Sales Analytics Dashboard.png` | Schematic only |

## Evidence rule

The presentation overview is not runtime business evidence. Claims are tied to executable source, tests, manifests, packaging configuration, methodology, and publication validation.
