# Contributing

Improvements are welcome as long as the project remains data-free, reproducible, and analytically explicit.

1. Create a focused branch.
2. Do not submit real company, customer, employee, financial-account, credential, or proprietary data.
3. Do not commit real, synthetic, dummy, or generated business datasets. Tests must use in-memory or automatically deleted temporary fixtures.
4. Add or update KPI documentation whenever analytical formulas change.
5. Preserve one central calculation definition for cards, charts, tables, insights, and exports.
6. Regenerate `app/index.html` only through `tools/prepare_app.mjs`; do not edit the generated file directly.
7. Run repository validation, privacy scanning, formula tests, and source/app parity checks before opening a pull request.
8. Describe analytical behavior changes clearly in `CHANGELOG.md`.

Recommended local check:

```bash
npm ci
npm test
npm run validate
npm run prepare-app
git diff --exit-code -- app/index.html app/generation-manifest.json
```
