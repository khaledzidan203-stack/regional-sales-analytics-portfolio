# Installation

## Fastest option: browser demo

Prerequisite: Python 3.

```bash
git clone <your-repository-url>
cd regional-sales-analytics-portfolio
python -m http.server 8000
```

Open:

```text
http://localhost:8000/src/
```

The dashboard automatically loads the synthetic files from `data/sample/`.

## Using npm

```bash
npm run dev
```

This uses the same Python HTTP server command defined in `package.json`.

## Optional Windows desktop build

The repository includes a Tauri 2 skeleton for reviewers who want to inspect desktop packaging. You need Node.js, Rust, the platform build toolchain, and Tauri prerequisites.

```bash
npm install
npm run desktop:build
```

The public portfolio does not ship compiled binaries in Git.
