# Recovery and Intervention Methodology

Users choose an intervention date plus explicit Pre and Post date ranges. Each range is paired with the same calendar dates in the previous year and can use Strict Comparable or Total Region scope.

```text
Pre LFL = (Pre Actual - Pre LY) / Pre LY
Post LFL = (Post Actual - Post LY) / Post LY
Momentum = Post LFL - Pre LFL

Expected Post = Post LY x (1 + Pre LFL)
Estimated Recovery = Actual Post - Expected Post
```

Budget shortfall is calculated for each period. Gap Compression is the Pre shortfall minus the Post shortfall. Branch and daily detail use the same selected windows.

The UI warns when Pre and Post durations differ, when a range crosses the intervention boundary unexpectedly, when prior-year support is missing, or when the selected period is invalid. Unequal durations do not silently become equivalent.

Estimated Recovery is a counterfactual analytical scenario: it compares actual Post sales with continuation of the Pre LFL trend. It is not causal proof and should be interpreted alongside operational context.
