# ADR-003: Local JavaScript Vendoring

**Status:** Accepted

Desktop generation replaces pinned CDN references with local Chart.js, datalabel, and XLSX bundles. This enables offline operation and avoids runtime CDN availability. Package locks and source-generation checks govern exact versions.
