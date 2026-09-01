# Desktop Architecture

```text
Generalized portfolio V12 source
  -> tools/prepare_app.mjs
  -> dependency URLs replaced with local vendor files
  -> desktop safe-area CSS injected
  -> app/index.html
  -> Tauri 2 command
  -> Rust/Wry host
  -> installed WebView2 Runtime
  -> Windows x64 desktop application
  -> optional NSIS installer
```

Release builds use the Windows GUI subsystem, so no console window opens. The main window starts maximized, remains resizable, disables devtools, and applies a restrictive local-content CSP. `app/index.html` is generated and must not be edited directly.

No executable or installer is published in the current release. See [release policy](../desktop_application/RELEASE_POLICY.md).
