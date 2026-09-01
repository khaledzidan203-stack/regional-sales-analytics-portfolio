# ADR-002: Tauri Desktop Packaging

**Status:** Accepted

Tauri 2 packages the local frontend through a small Rust/Wry host. It provides a Windows-native executable and NSIS path while reusing the analytical frontend. WebView2 is the Windows rendering dependency.
