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
