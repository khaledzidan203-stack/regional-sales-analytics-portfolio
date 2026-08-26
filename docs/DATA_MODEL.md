# Data Model

## Logical model

```text
Branch Master (1) ───────────────< Daily Sales (*)
      │                                │
      │                                ├── Date
      │                                └── Branch
      │
      ├──────────────────────────< Monthly Budget (*)
      │                                ├── Month
      │                                └── Branch
      │
      └──────────────────────────< Delivery Channel (*)
                                       ├── Date
                                       └── Branch
```

## Grain

- **Branch Master:** one row per branch.
- **Daily Sales:** one row per date + branch after normalization. The sample intentionally contains a duplicate source row so Data Quality can detect it.
- **Monthly Budget:** one row per month + branch.
- **Delivery Channel:** one row per date + branch with channel activity.

## Keys

- Branch key: `Branch`.
- Daily composite key: `Date + Branch`.
- Monthly target key: `Month + Branch`.

## Lifecycle

`Opening Date` and `Closing Date` support strict comparable-branch logic. A branch is considered comparable only when it exists across the relevant LY/current comparison windows.

## Analytical relationship rule

Delivery Channel is modeled as a **component** of Core Retail Sales. This relationship is deliberately documented to prevent double counting.
