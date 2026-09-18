CREATE TABLE retail_financial_info (
    company TEXT,
    ticker TEXT,
    fiscal_year INT,
    revenue BIGINT,
    cogs BIGINT,
    receivable_accounts BIGINT,
    inventory BIGINT,
    payable_accounts BIGINT,
    current_assets BIGINT,
    current_liabilities BIGINT,
    working_capital BIGINT,
    current_ratio NUMERIC(4,2),
    dio NUMERIC(6,2),
    dpo NUMERIC(6,2),
    dso NUMERIC(6,2),
    cash_conversion_cycle NUMERIC(6,2)
);

SELECT COUNT(*)
FROM retail_financial_info;

SELECT *
FROM retail_financial_info
LIMIT 5;