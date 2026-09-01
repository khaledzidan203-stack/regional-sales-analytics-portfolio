# Installation

## Source review

Prerequisite: Python 3.

```bash
git clone <your-repository-url>
cd regional-sales-analytics-portfolio
npm ci
npm run prepare-app
python -m http.server 8000
```

Open:

```text
http://localhost:8000/app/
```

The application opens in an empty state. Business input files are selected locally at runtime and are not included in the repository.

## Using npm

```bash
npm run dev
```

This uses the same Python HTTP server command defined in `package.json`.

## Optional Windows desktop build

The repository includes a Tauri 2 skeleton for reviewers who want to inspect desktop packaging. You need Node.js, Rust, the platform build toolchain, and Tauri prerequisites.

```bash
npm ci
npm run desktop:build
```

The public portfolio does not ship compiled binaries or business datasets in Git.
