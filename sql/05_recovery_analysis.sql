-- Recovery scenario. Parameters define explicit Pre/Post and prior-year windows.
WITH period_totals AS (
    SELECT
        SUM(CASE WHEN sales_date BETWEEN :pre_from AND :pre_to THEN core_retail_sales + service_channel_sales ELSE 0 END) AS pre_sales,
        SUM(CASE WHEN sales_date BETWEEN :pre_ly_from AND :pre_ly_to THEN core_retail_sales + service_channel_sales ELSE 0 END) AS pre_ly_sales,
        SUM(CASE WHEN sales_date BETWEEN :post_from AND :post_to THEN core_retail_sales + service_channel_sales ELSE 0 END) AS post_sales,
        SUM(CASE WHEN sales_date BETWEEN :post_ly_from AND :post_ly_to THEN core_retail_sales + service_channel_sales ELSE 0 END) AS post_ly_sales
    FROM fact_sales_daily
), metrics AS (
    SELECT *,
        CASE WHEN pre_ly_sales = 0 THEN NULL ELSE (pre_sales - pre_ly_sales) * 1.0 / pre_ly_sales END AS pre_lfl,
        CASE WHEN post_ly_sales = 0 THEN NULL ELSE (post_sales - post_ly_sales) * 1.0 / post_ly_sales END AS post_lfl
    FROM period_totals
)
SELECT *,
       post_lfl - pre_lfl AS momentum,
       post_ly_sales * (1 + pre_lfl) AS expected_post,
       post_sales - post_ly_sales * (1 + pre_lfl) AS estimated_recovery
FROM metrics;
