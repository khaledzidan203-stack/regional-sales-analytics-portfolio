# ADR-001: Single-file Analytical Source

**Status:** Accepted

The analytical UI, state, calculations, and presentation remain in one HTML source. This keeps portable review and offline delivery simple. The cost is file size, so central named functions and validation tests are required to prevent logic drift.
