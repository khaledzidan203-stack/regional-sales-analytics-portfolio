-- Strict comparable-branch LFL pattern.
-- Parameters: :current_from, :current_to, :ly_from, :ly_to
WITH comparable AS (
    SELECT branch_id
    FROM dim_branch
    WHERE (opening_date IS NULL OR opening_date <= :ly_from)
      AND (closing_date IS NULL OR closing_date >= :current_to)
),
current_period AS (
    SELECT branch_id,
           SUM(core_retail_sales + service_channel_sales) AS sales
    FROM fact_sales_daily
    WHERE sales_date BETWEEN :current_from AND :current_to
      AND branch_id IN (SELECT branch_id FROM comparable)
    GROUP BY branch_id
),
ly_period AS (
    SELECT branch_id,
           SUM(core_retail_sales + service_channel_sales) AS sales
    FROM fact_sales_daily
    WHERE sales_date BETWEEN :ly_from AND :ly_to
      AND branch_id IN (SELECT branch_id FROM comparable)
    GROUP BY branch_id
)
SELECT
    COALESCE(c.branch_id, l.branch_id) AS branch_id,
    COALESCE(c.sales, 0) AS current_sales,
    COALESCE(l.sales, 0) AS ly_sales,
    CASE WHEN COALESCE(l.sales, 0) = 0 THEN NULL
         ELSE (COALESCE(c.sales, 0) - l.sales) * 1.0 / l.sales
    END AS lfl_growth
FROM current_period c
LEFT JOIN ly_period l ON l.branch_id = c.branch_id
ORDER BY lfl_growth;
