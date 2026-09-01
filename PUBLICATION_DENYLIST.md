# Publication Denylist

The following must not be committed, published, attached to a release, or included in screenshots:

- `node_modules/`, `src-tauri/target/`, `target/`, private build caches, and generated compiler metadata
- `*.exe`, `*.msi`, `*.pdb`, `*.map`, archives, backups, and temporary files
- Real or synthetic CSV/XLSX inputs, dummy/generated business datasets, business exports, sales, budgets, customer counts, or branch performance data
- Internal operational reports, company-only documentation, and private screenshots
- Credentials, tokens, passwords, API keys, certificates, and private keys
- Absolute private machine paths and internal hostnames
- Company branding, logos, names, internal area identifiers, real branch codes, and proprietary assets

Release binaries may be reconsidered only after a generalized data-free rebuild passes the documented release gates. Existing private binaries remain denied.
