# KPI Definitions

| KPI | Definition | Formula / rule |
|---|---|---|
| Total Sales | Recorded sales across the two primary segments | Core Retail Sales + Service Channel Sales |
| Core Retail Sales | Main retail segment sales | Sum of `Core Retail Sales` |
| Service Channel Sales | Secondary service segment sales | Sum of `Service Channel Sales` |
| Priority Sales | Selected strategic product/program sales | Sum of `Priority Sales` |
| Customer Count | Recorded transactions/customers | Sum of `Customer Count` |
| AST | Average sales per customer | Total Sales / Customer Count |
| Budget | Target for selected period | Monthly budget prorated by selected calendar days |
| Achievement | Actual vs target | Total Sales / Budget |
| Budget Gap | Absolute difference to target | Total Sales - Budget |
| Core Retail Achievement | Core actual vs core budget | Core Retail Sales / Core Retail Budget |
| Service Achievement | Service actual vs service budget | Service Channel Sales / Service Channel Budget |
| Priority Rate | Priority contribution within core retail | Priority Sales / Core Retail Sales |
| Service Mix | Service contribution to total sales | Service Channel Sales / Total Sales |
| LFL Growth | Current performance vs same period last year | (Current - LY) / LY |
| Strict LFL | LFL on lifecycle-comparable branches only | Excludes branches not open across both comparison windows or closed before current-period end |
| Total LFL | LFL under current filters without lifecycle exclusion | Current selected scope vs same calendar period LY |
| Pre LFL | LFL for pre-intervention window | (Pre - Pre LY) / Pre LY |
| Post LFL | LFL for post-intervention window | (Post - Post LY) / Post LY |
| Momentum | Change in YoY performance after intervention | Post LFL - Pre LFL, expressed in percentage points |
| Expected Post | Scenario if pre-trend continued | Post LY × (1 + Pre LFL) |
| Estimated Recovery | Sales above/below expected-post scenario | Actual Post - Expected Post |
| Delivery % of Core Retail | Delivery-channel component penetration | Delivery Channel Sales / Core Retail Sales |
| Core Retail ex-Delivery | Analytical counterfactual | Core Retail Sales - Delivery Channel Sales |

## Interpretation rules

- AST is weighted using total sales divided by total customers; daily AST values are not averaged.
- Partial-month budget comparisons are prorated by calendar days in scope.
- Estimated Recovery is a counterfactual scenario indicator and **not proof of causality**.
- Delivery-channel sales are already embedded within core retail in the synthetic model, so they are never added again to total sales.
