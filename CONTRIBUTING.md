# Contributing

This repository is primarily a portfolio project, but improvements are welcome.

1. Fork the repository and create a focused branch.
2. Do not submit real company, customer, employee, healthcare, financial-account, credential, or proprietary data.
3. Keep sample data synthetic and document any new fields in `docs/DATA_DICTIONARY.md`.
4. Add or update KPI definitions when analytical formulas change.
5. Validate that the dashboard still loads with the files in `data/sample/`.
6. Run a privacy scan before opening a pull request.
7. Describe analytical behavior changes clearly in `CHANGELOG.md`.

For formula changes, keep one calculation definition and reuse it across KPIs, charts, tables, and exports whenever possible.
