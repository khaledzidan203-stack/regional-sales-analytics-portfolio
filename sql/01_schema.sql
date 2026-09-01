-- Generalized logical schema. The repository intentionally provides no data rows.
CREATE TABLE dim_branch (
    branch_id TEXT PRIMARY KEY,
    branch_name TEXT NOT NULL,
    city TEXT NOT NULL,
    category TEXT NOT NULL,
    size_sqm REAL,
    opening_date DATE,
    closing_date DATE
);

CREATE TABLE fact_sales_daily (
    sales_date DATE NOT NULL,
    branch_id TEXT NOT NULL,
    core_retail_sales DECIMAL(18,2) NOT NULL,
    service_channel_sales DECIMAL(18,2) NOT NULL,
    priority_sales DECIMAL(18,2) NOT NULL,
    customer_count INTEGER NOT NULL,
    PRIMARY KEY (sales_date, branch_id),
    FOREIGN KEY (branch_id) REFERENCES dim_branch(branch_id)
);

CREATE TABLE fact_budget_monthly (
    month_key TEXT NOT NULL,
    branch_id TEXT NOT NULL,
    total_budget DECIMAL(18,2) NOT NULL,
    core_retail_budget DECIMAL(18,2) NOT NULL,
    service_channel_budget DECIMAL(18,2) NOT NULL,
    PRIMARY KEY (month_key, branch_id),
    FOREIGN KEY (branch_id) REFERENCES dim_branch(branch_id)
);

CREATE TABLE fact_delivery_channel (
    sales_date DATE NOT NULL,
    branch_id TEXT NOT NULL,
    delivery_channel_sales DECIMAL(18,2) NOT NULL,
    PRIMARY KEY (sales_date, branch_id),
    FOREIGN KEY (branch_id) REFERENCES dim_branch(branch_id)
);
