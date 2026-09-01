# KPI Dictionary

All ratios use aggregated numerators and denominators. Currency and percentage formatting is presentation-only.

| KPI | Definition / formula | Grain | Interpretation | Limitations |
|---|---|---|---|---|
| Total Sales | `Core Retail + Service Channel` | Date x Branch, aggregatable | Recorded sales | Delivery must not be added again |
| Budget | Sum of prorated monthly total targets | Month x Branch | Expected performance | Depends on available target months |
| Achievement | `Actual in budget-covered dates / Budget` | Filter context | Share of target delivered | Undefined when budget is zero |
| Gap | `Actual in budget-covered dates - Budget` | Filter context | Currency over/under target | Not comparable without scope context |
| Core Retail Sales | Recorded base retail component | Date x Branch | Underlying retail activity | Includes Delivery Channel |
| Service Channel Sales | Recorded service component | Date x Branch | Service activity | May include valid negative returns |
| Core Retail Budget | Sum of Core Retail targets | Month x Branch | Segment expectation | Subject to date proration |
| Service Channel Budget | Sum of Service Channel targets | Month x Branch | Segment expectation | Subject to date proration |
| Segment Achievement | `Segment actual / segment budget` | Filter context | Segment target attainment | Undefined at zero target |
| Priority Sales | Recorded priority subset | Date x Branch | Priority-product contribution | Must use the same accounting basis as Core Retail |
| Priority Rate | `Priority Sales / Core Retail Sales` | Filter context | Priority contribution | Undefined at zero Core Retail |
| Customer Count | Sum of recorded transactions/customers | Date x Branch | Traffic volume | Source definition must remain consistent |
| AST | `Total Sales / Customer Count` | Filter context | Weighted average sale per transaction | Undefined at zero customers; never average row ASTs |
| Service Channel Mix | `Service Channel / Total Sales` | Filter context | Service share | Distorted when total is zero |
| Core Retail Mix | `Core Retail / Total Sales` | Filter context | Core share | Complements Service mix when inputs reconcile |
| LFL Growth | `(Current - aligned LY) / aligned LY` | Selected period/scope | Comparable direction | Undefined at zero LY; not causal |
| Pre LFL | LFL over selected Pre window | Pre period | Baseline trend | Sensitive to window choice |
| Post LFL | LFL over selected Post window | Post period | Later trend | Sensitive to window choice |
| Momentum | `Post LFL - Pre LFL` | Recovery analysis | Change in percentage points | Association, not causal proof |
| Expected Post | `Post LY x (1 + Pre LFL)` | Recovery analysis | Counterfactual continuation | Requires a valid prior-year base |
| Estimated Recovery | `Actual Post - Expected Post` | Recovery analysis | Sales above/below scenario | Scenario estimate only |
| Budget Shortfall | `(Budget - Actual) / Budget` | Period | Relative underperformance | Undefined at zero budget |
| Gap Compression | `Pre shortfall - Post shortfall` | Recovery analysis | Improvement in percentage points | Period duration and scope matter |
| Delivery Sales | Recorded embedded component | Date x Branch | Direct channel contribution | Already included in Core Retail |
| Delivery Penetration | `Delivery / Core Retail` | Filter context | Component share of Core Retail | Matching/accounting basis must align |
| Core Retail ex-Delivery | `Core Retail - Delivery` | Filter context | Analytical counterfactual | Not a separately recorded sales measure |
| Delivery LFL Uplift | `Core Retail LFL with Delivery - ex-Delivery LFL` | LFL scope | Contribution to growth rate | Requires aligned Delivery history |
| Budget Gap Recovery | Reduction in hypothetical Core Retail shortfall attributable to Delivery | Filter context | Portion of gap offset | Counterfactual, not incremental revenue proof |
| Data Readiness Score | Weighted deductions from 100 for confirmed quality exceptions | Loaded model | Triage indicator | Not a substitute for source reconciliation |
