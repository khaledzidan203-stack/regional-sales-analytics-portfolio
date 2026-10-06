# Desktop Architecture

```text
Generalized V12 analytical source
  -> tools/prepare_app.mjs
  -> required browser dependencies localized
  -> desktop safe-area CSS injected
  -> app/index.html
  -> Tauri CLI
  -> Rust / Wry host
  -> installed WebView2 Runtime
  -> Windows x64 desktop application
  -> optional NSIS bundle
```

## Current packaging configuration

- Application version: 1.0.2
- Tauri Rust crate: 2.11.5
- Tauri CLI: 2.8.4
- tauri-build: 2.6.3
- Windows GUI subsystem
- maximized startup
- resizable main window
- devtools disabled
- restrictive local-content CSP
- NSIS target

`app/index.html` is generated and must not be edited directly.

## Evidence boundary

The repository contains desktop packaging source and a reproducibly generated frontend.

No public executable or installer is committed, and the current Linux-based GitHub validation workflow does not prove a clean Windows installation.
