# Delivery Channel Methodology

Delivery Channel is an embedded component of Core Retail Sales.

```text
Total Sales = Core Retail + Service Channel
Core Retail ex-Delivery = Core Retail - Delivery Channel
```

Delivery is never added to Total Sales. Introducing Delivery data changes contribution and counterfactual analysis, not recorded total revenue.

The application measures Delivery penetration, active Delivery branches, With-Delivery versus ex-Delivery Core Retail LFL, growth uplift, budget-achievement uplift, hypothetical gap recovery, and branch-level contribution. Matching uses Date x Branch.

Quality checks identify invalid rows, duplicates, missing branch mappings, unmatched sales rows, negative Delivery amounts, and Delivery amounts exceeding matched Core Retail. The component file must use the same accounting basis and date/branch identifiers as the sales source.
