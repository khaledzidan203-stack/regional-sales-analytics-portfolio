-- Delivery is already included within Core Retail and must not be added to Total Sales.
SELECT
    s.sales_date,
    s.branch_id,
    s.core_retail_sales + s.service_channel_sales AS total_sales,
    s.core_retail_sales,
    COALESCE(d.delivery_channel_sales, 0) AS delivery_channel_sales,
    s.core_retail_sales - COALESCE(d.delivery_channel_sales, 0) AS core_retail_ex_delivery,
    CASE WHEN s.core_retail_sales = 0 THEN NULL
         ELSE COALESCE(d.delivery_channel_sales, 0) * 1.0 / s.core_retail_sales
    END AS delivery_penetration
FROM fact_sales_daily s
LEFT JOIN fact_delivery_channel d
  ON d.sales_date = s.sales_date AND d.branch_id = s.branch_id;
