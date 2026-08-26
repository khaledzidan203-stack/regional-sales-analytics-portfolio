# Power BI Mapping

No `.pbix` file is included in this repository. This document shows how the public data model and formulas map directly to a Power BI implementation.

## Recommended star schema

- `DimBranch` ← `branch_master.csv`
- `DimDate` ← generated calendar table
- `FactSales` ← `sales_daily.csv`
- `FactBudget` ← `monthly_budget.csv`
- `FactDelivery` ← `delivery_channel.csv`

Relationships:
- `DimBranch[Branch]` 1:* to all fact tables.
- `DimDate[Date]` 1:* to `FactSales[Date]` and `FactDelivery[Date]`.
- `FactBudget[Month]` can be related through a month-start key or a dedicated month dimension.

## Example DAX measures

```DAX
Total Sales =
SUM(FactSales[Core Retail Sales]) +
SUM(FactSales[Service Channel Sales])
```

```DAX
Customer Count = SUM(FactSales[Customer Count])
```

```DAX
AST = DIVIDE([Total Sales], [Customer Count])
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
LFL Growth = DIVIDE([Total Sales] - [Sales LY], [Sales LY])
```

Strict LFL requires a comparable-branch flag based on opening/closing lifecycle dates. In Power BI this can be implemented using measures that test each branch against current and prior period boundaries, then apply the eligible branch set through `TREATAS` or filtered branch iterators.

## Visual mapping

- KPI Cards → Card visuals.
- Sales by City / Branch → clustered bar charts.
- LFL trend → line chart with current and LY measures.
- Budget Gap → bar chart with conditional color formatting.
- Traffic / AST segmentation → scatter plot or quadrant visual.
- Data Quality → table with issue slicer and severity formatting.
- Intervention Impact → cards + line/column comparison using disconnected parameter dates if full flexibility is required.
