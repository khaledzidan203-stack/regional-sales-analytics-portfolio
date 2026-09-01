-- Duplicate source grain.
SELECT sales_date, branch_id, COUNT(*) AS row_count
FROM fact_sales_daily
GROUP BY sales_date, branch_id
HAVING COUNT(*) > 1;

-- Sales without master mapping.
SELECT s.*
FROM fact_sales_daily s
LEFT JOIN dim_branch b ON b.branch_id = s.branch_id
WHERE b.branch_id IS NULL;

-- Sales with zero customer count.
SELECT *
FROM fact_sales_daily
WHERE customer_count = 0
  AND (core_retail_sales + service_channel_sales) <> 0;

-- Priority sales should not exceed their parent core-retail segment.
SELECT *
FROM fact_sales_daily
WHERE priority_sales > core_retail_sales;

-- Lifecycle conflicts.
SELECT s.*
FROM fact_sales_daily s
JOIN dim_branch b ON b.branch_id = s.branch_id
WHERE (b.opening_date IS NOT NULL AND s.sales_date < b.opening_date)
   OR (b.closing_date IS NOT NULL AND s.sales_date > b.closing_date);

-- Delivery rows without a matching parent sales row or exceeding Core Retail.
SELECT d.*, s.core_retail_sales
FROM fact_delivery_channel d
LEFT JOIN fact_sales_daily s
  ON s.sales_date = d.sales_date AND s.branch_id = d.branch_id
WHERE s.branch_id IS NULL OR d.delivery_channel_sales > s.core_retail_sales;
