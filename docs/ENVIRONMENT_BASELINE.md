# Environment Baseline

## Application version

- Application: 1.0.2

## Browser analytical layer

- HTML5
- CSS3
- JavaScript
- Chart.js 4.4.1
- chartjs-plugin-datalabels 2.2.0
- xlsx-js-style 1.2.0

The generalized source references the required browser packages. The generated desktop frontend replaces those dependency URLs with files under `app/vendor/`.

## Node / desktop tooling

- Node.js 22 in GitHub Actions
- Tauri CLI 2.8.4
- Tauri Rust crate 2.11.5
- tauri-build 2.6.3
- Rust edition 2021
- Wry/WebView2 host path through Tauri
- NSIS x64 bundle target

## Python validation

- Python 3.12 in GitHub Actions
- test and validation code uses Python standard-library functionality

## Data boundary

No business data dependency is installed or downloaded by CI.

## Local commands

```bash
npm ci
npm test
npm run validate
npm run prepare-app
```

Optional Windows packaging requires the Rust MSVC toolchain, platform prerequisites and WebView2 availability.
