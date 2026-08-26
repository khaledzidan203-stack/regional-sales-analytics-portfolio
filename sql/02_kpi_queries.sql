-- Core KPI pattern. Syntax is intentionally portable; date functions may need adjustment by SQL engine.
SELECT
    SUM(core_retail_sales + service_channel_sales) AS total_sales,
    SUM(core_retail_sales) AS core_retail_sales,
    SUM(service_channel_sales) AS service_channel_sales,
    SUM(priority_sales) AS priority_sales,
    SUM(customer_count) AS customer_count,
    CASE WHEN SUM(customer_count) = 0 THEN NULL
         ELSE SUM(core_retail_sales + service_channel_sales) * 1.0 / SUM(customer_count)
    END AS ast,
    CASE WHEN SUM(core_retail_sales) = 0 THEN NULL
         ELSE SUM(priority_sales) * 1.0 / SUM(core_retail_sales)
    END AS priority_rate
FROM fact_sales_daily
WHERE sales_date BETWEEN :date_from AND :date_to;

-- Branch performance ranking.
SELECT
    s.branch_id,
    b.city,
    SUM(s.core_retail_sales + s.service_channel_sales) AS sales,
    SUM(s.customer_count) AS customers,
    CASE WHEN SUM(s.customer_count) = 0 THEN NULL
         ELSE SUM(s.core_retail_sales + s.service_channel_sales) * 1.0 / SUM(s.customer_count)
    END AS ast
FROM fact_sales_daily s
JOIN dim_branch b ON b.branch_id = s.branch_id
WHERE s.sales_date BETWEEN :date_from AND :date_to
GROUP BY s.branch_id, b.city
ORDER BY sales DESC;
