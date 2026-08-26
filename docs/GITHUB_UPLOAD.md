# GitHub Upload Instructions

## Option A — GitHub website

1. Sign in to GitHub.
2. Click **New repository**.
3. Repository name suggestion: `regional-sales-analytics-portfolio`.
4. Add a short description such as: `Interactive retail sales analytics portfolio: KPI, budget gap, LFL, intervention impact, channel contribution and data quality.`
5. Choose **Public**.
6. Do **not** initialize with a README, license, or `.gitignore` because these files already exist locally.
7. Create the repository.
8. On the empty-repository page choose **uploading an existing file**.
9. Upload the contents of this repository folder, preserving the directory structure.
10. Commit with a message such as `Initial public portfolio release`.

The command-line method below is preferable because it preserves the repository structure more reliably.

## Option B — Git command line (recommended)

Open Terminal / PowerShell inside the unzipped repository folder:

```bash
git init
git add .
git commit -m "Initial public portfolio release"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/regional-sales-analytics-portfolio.git
git push -u origin main
```

If Git asks for authentication, use GitHub's browser/device authentication flow or a supported personal access token. Do not store credentials inside this repository.

## After upload

1. Open the repository on GitHub and confirm the README renders correctly.
2. Open the three screenshot images from the README.
3. Verify `data/sample/` contains only synthetic data.
4. Check the **Actions** tab and confirm `Validate portfolio repository` passes.
5. Add repository topics such as `data-analysis`, `business-analysis`, `javascript`, `sql`, `power-bi`, `analytics`, `dashboard`, `tauri`.
6. In **About**, optionally add a concise description and your portfolio/GitHub Pages link later.
7. Pin the repository on your GitHub profile.

## Optional GitHub Pages demo

Because the dashboard reads files using relative paths, the easiest Pages layout is to publish the repository root and open `/src/`. If using GitHub Pages from the `main` branch, select **Settings → Pages → Deploy from a branch → main / root**. The public URL will then be similar to:

```text
https://YOUR-USERNAME.github.io/regional-sales-analytics-portfolio/src/
```

If Pages behavior changes, use a simple static host that serves the repository root without changing relative paths.
