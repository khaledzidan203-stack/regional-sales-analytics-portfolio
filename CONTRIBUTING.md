# Contributing

This repository is primarily a portfolio project, but improvements are welcome.

1. Fork the repository and create a focused branch.
2. Do not submit real company, customer, employee, healthcare, financial-account, credential, or proprietary data.
3. Do not submit real, synthetic, dummy, or generated business datasets. Tests must use in-memory or automatically deleted temporary fixtures.
4. Add or update KPI definitions when analytical formulas change.
5. Validate the generalized source, generated frontend, and formula tests without committing input files.
6. Run a privacy scan before opening a pull request.
7. Describe analytical behavior changes clearly in `CHANGELOG.md`.

For formula changes, keep one calculation definition and reuse it across KPIs, charts, tables, and exports whenever possible.
