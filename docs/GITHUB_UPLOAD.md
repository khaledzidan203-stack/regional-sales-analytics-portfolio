# Repository Setup, Validation & Pages

This repository is already structured for automated validation and static GitHub Pages review.

## Local validation

Before pushing a change:

```bash
npm ci
npm test
npm run validate
npm run prepare-app
git diff --exit-code -- app/index.html app/generation-manifest.json
```

## Generated frontend rule

`app/index.html` is generated from:

`source/Regional_Sales_Performance_V12_PORTFOLIO.html`

Do not edit the generated frontend as the authoritative source.

After any generalized-source change, run:

```bash
npm run prepare-app
```

and commit both:

- `app/index.html`
- `app/generation-manifest.json`

## GitHub Actions

The workflow:

`.github/workflows/validate.yml`

checks repository structure, privacy/publication rules, analytical regression tests, source/app parity, page count, versions, local desktop dependencies, and Markdown links.

## GitHub Pages

The repository can be reviewed in its data-free upload state at:

`https://khaledzidan203-stack.github.io/regional-sales-analytics-portfolio/app/`

The interface remains empty until the user selects compatible local input files.

## Publication checklist

Before release:

- confirm no business data file has been committed;
- confirm no business-result screenshot has been added;
- confirm no binary/installer artifact has been added;
- confirm privacy scanning passes;
- confirm analytical tests pass;
- confirm source/app regeneration produces zero diff;
- manually review the final staged diff.
