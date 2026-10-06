# Sanitization Manifest

This manifest records the publication status of the generalized public source.

| Public Artifact | Status | Publication Rule | Validation |
|---|---|---|---|
| `source/Regional_Sales_Performance_V12_PORTFOLIO.html` | APPROVED GENERALIZED SOURCE | No embedded business rows, private identifiers, logo assets, private paths or blocked terminology | Privacy scan, source tests, JavaScript syntax |
| `app/index.html` | GENERATED / APPROVED | Must be regenerated from the generalized source; never edited as the authoritative source | Source/app SHA-256 manifest + zero-diff generation |
| `app/vendor/` | APPROVED LOCAL DEPENDENCIES | Only reviewed package artifacts required for offline runtime | Presence and offline-reference checks |
| `src-tauri/` | APPROVED SOURCE | Packaging source only; no compiled artifacts | Version/configuration checks |
| `package.json` / lockfile | APPROVED METADATA | Public dependency/build metadata only | Version and dependency review |
| `tools/` | APPROVED SOURCE | Generalized analytics helpers, generation, validation and privacy controls | CI execution |
| `tests/` | APPROVED TESTS | In-memory or temporary fixtures only | CI execution |
| `sql/` | APPROVED REFERENCE | Engine-neutral generalized analytical logic only | Documentation/source review |
| `docs/` | APPROVED DOCUMENTATION | No business figures or reverse mapping to private terminology | Link + privacy validation |
| `docs/assets/Regional Sales Analytics Dashboard.png` | APPROVED SCHEMATIC | Placeholder/illustrative visual only; not business-result evidence | Manual review + repository size cap |
| Executables / installers | DENIED IN CURRENT RELEASE | Do not publish until binary release gates pass | Future Windows/binary validation required |
| Business datasets | DENIED | No real, synthetic, dummy or generated business dataset | Artifact scan |
| Analytical result screenshots | DENIED | No screenshots containing business figures | Artifact/publication review |

## Core rule

Public artifacts are generalized or generated from generalized source. No private output is copied automatically into the public release.
