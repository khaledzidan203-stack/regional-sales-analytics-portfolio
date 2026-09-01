# Sanitization Manifest

No source is transferred automatically. `Pending review` means the item is not approved for publication.

| Source Item | Classification | Destination | Action | Sanitization Required | Validation Required | Notes |
|---|---|---|---|---|---|---|
| Private V12 analytical HTML | SANITIZE FIRST | `source/Regional_Sales_Performance_V12_PORTFOLIO.html` | Reproducibly generalize identifiers and labels | Yes | Privacy, logic, schema, UI, and in-memory tests | No embedded logo or records |
| Private generated frontend | GENERATED / DENIED | `app/index.html` | Regenerate from public source | Yes | Reproducibility, offline, and parity checks | Never copied directly |
| Private Tauri/Rust architecture | SANITIZE FIRST | `src-tauri/` | Recreate from verified configuration | Yes | Package/version/build validation | No private icons or target metadata |
| `src-tauri/tauri.conf.json` | SANITIZE FIRST | `src-tauri/tauri.conf.json` | Curate later | Yes | CSP, bundle, window, and installer validation | Remove unapproved branding |
| `src-tauri/src/main.rs` | REVIEW | `src-tauri/src/main.rs` | Review before reuse | Possibly | Console/subsystem and entry-point checks | Small Rust entry point |
| `src-tauri/src/lib.rs` | REVIEW | `src-tauri/src/lib.rs` | Review before reuse | Possibly | Tauri startup smoke test | No transfer in this phase |
| `package.json` | SANITIZE FIRST | `package.json` | Update later | Yes | Dependency, version, and script validation | Align with portfolio identity and V12 dependencies |
| Private prepare-app pattern | SANITIZE FIRST | `tools/prepare_app.mjs` | Recreate for public source | Yes | Deterministic generation and path scan | Targets generalized source only |
| `BUILD_FINAL.bat` | SANITIZE FIRST | `scripts/build-windows.bat` | Replace later | Yes | Clean-machine build test | Remove private wording and shell-launch behavior as needed |
| `README_FINAL_AR.txt` | DOCUMENTATION / SANITIZE FIRST | `docs/desktop_application/` | Rewrite later | Yes | Documentation and path scan | Do not copy verbatim during foundation phase |
| Private icons/assets | DO NOT PUBLISH | None | Exclude | Yes | Logo and asset scan | Generic text identity only |
