# Publication Denylist

The following must not be committed, published, attached to a release, or presented as public analytical evidence:

- `node_modules/`, `src-tauri/target/`, `target/`, private build caches, and generated compiler metadata;
- `*.exe`, `*.msi`, `*.pdb`, `*.map`, archives, backups, and temporary build artifacts;
- real or synthetic CSV/XLSX business inputs;
- dummy/generated business datasets;
- business exports, sales, budgets, customer counts, or branch-performance records;
- internal operational reports and company-only documentation;
- analytical-result screenshots containing business figures;
- credentials, tokens, passwords, API keys, certificates, and private keys;
- absolute private machine paths and internal hostnames;
- company branding, logos, names, internal geographic identifiers, real branch codes, and proprietary assets.

The reviewed abstract presentation image under `docs/assets/` is permitted by the allowlist because it contains only placeholder/illustrative visuals and is not an analytical-result screenshot.

Release binaries may be reconsidered only after a generalized data-free rebuild passes the documented release gates. Existing private binaries remain denied.
