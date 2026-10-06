# Power BI Implementation Blueprint

> **Implementation status — design/mapping only.** No PBIX, PBIP, PBIR, TMDL or PBIT runtime artifact is committed.

This document maps the generalized analytical model to a possible Power BI implementation using privately managed source data.

## Recommended star schema

- `DimBranch` ← Branch Master input
- `DimDate` ← generated calendar table
- `FactSales` ← Sales Collection input
- `FactBudget` ← Budget Breakdown input
- `FactDelivery` ← optional Delivery Channel input

Recommended relationships:

- `DimBranch[Branch]` 1:* to all fact tables.
- `DimDate[Date]` 1:* to `FactSales[Date]` and `FactDelivery[Date]`.
- Monthly budget should use a month-start key or dedicated month dimension.

## Example DAX

```DAX
Total Sales =
SUM(FactSales[Core Retail Sales]) +
SUM(FactSales[Service Channel Sales])
```

```DAX
Customer Count =
SUM(FactSales[Customer Count])
```

```DAX
AST =
DIVIDE([Total Sales], [Customer Count])
```

```DAX
Priority Rate =
DIVIDE(
    SUM(FactSales[Priority Sales]),
    SUM(FactSales[Core Retail Sales])
)
```

```DAX
Service Mix =
DIVIDE(
    SUM(FactSales[Service Channel Sales]),
    [Total Sales]
)
```

```DAX
Sales LY =
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(DimDate[Date])
)
```

```DAX
LFL Growth =
DIVIDE([Total Sales] - [Sales LY], [Sales LY])
```

## Strict comparable design

Strict LFL requires a comparable-branch set based on opening/closing lifecycle dates and the current/prior comparison windows.

Possible implementation patterns include:

- filtered branch iterators;
- a comparable flag at the selected window;
- `TREATAS` applied to the eligible branch set.

The exact implementation should be reconciled to the browser engine before runtime equivalence is claimed.

## Suggested visual mapping

- KPI cards → Card visuals
- Sales by City / Branch → clustered bars
- LFL trend → line charts
- Budget Gap → variance bars
- Traffic / AST segmentation → scatter/quadrant
- Data Quality → detailed table with severity
- Recovery → Pre/Post cards and trend comparison

## Evidence boundary

The browser/desktop analytical source is the implemented runtime logic in this repository.

Power BI is a blueprint only until a source-controlled model and retained reconciliation evidence are added.
