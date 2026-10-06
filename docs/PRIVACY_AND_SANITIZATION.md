# Privacy and Sanitization

This repository is a generalized public analytical release, not a copy of a production repository.

## Removed or excluded

- Real company name and branding.
- Real geographic operating labels.
- Real branch/store identifiers and names.
- Real customer or transaction records.
- Employee information.
- Identity or other personal records.
- Passwords, credentials, tokens, API keys, connection strings and server addresses.
- Internal installer binaries and private deployment paths.
- Proprietary source datasets.
- Organization-specific action owners, commercial thresholds and operating instructions.

## Generalized

- Business segments are represented as Core Retail, Service Channel, Priority Sales and Delivery Channel.
- Geography and branch identifiers are provided only at runtime and are not committed.
- Organization-specific owners, thresholds and review cadence are excluded.
- Data Quality rules are expressed as broadly reusable controls.

## Data-free repository

No real, synthetic, dummy or generated business dataset is included.

Tests use in-memory objects or temporary files removed automatically.

Analytical result screenshots with business figures are excluded.

The overview graphic under `docs/assets/` is an abstract presentation schematic and is not a business-result screenshot.

## Publication controls

Automated validation checks:

- forbidden business-data file types and directories;
- private-domain terminology;
- embedded branding;
- credentials;
- private filesystem paths;
- internal network addresses;
- broken documentation links;
- source/app parity.
