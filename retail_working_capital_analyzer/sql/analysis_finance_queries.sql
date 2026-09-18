SELECT
    company,
    ROUND(AVG(dio), 2) AS avg_dio,
    ROUND(AVG(dpo), 2) AS avg_dpo,
    ROUND(AVG(dso), 2) AS avg_dso,
    ROUND(AVG(cash_conversion_cycle), 2) AS avg_ccc
FROM
    retail_financial_info
GROUP BY 
    company
ORDER BY 
    avg_ccc;

SELECT
    company,
    fiscal_year,
    cash_conversion_cycle
FROM 
    retail_financial_info
ORDER BY 
    company, fiscal_year;

SELECT
    company,
    fiscal_year,
    cash_conversion_cycle,
    LAG(cash_conversion_cycle) OVER (
        PARTITION BY company
        ORDER BY fiscal_year
    ) AS previous_year_ccc,
    ROUND(
        cash_conversion_cycle - LAG(cash_conversion_cycle) OVER (
            PARTITION BY company
            ORDER BY fiscal_year
        ),
        2
    ) AS yty_change
FROM retail_financial_info
ORDER BY company, fiscal_year;

SELECT
    company,
    fiscal_year,
    cash_conversion_cycle,
    RANK() OVER (
        PARTITION BY fiscal_year
        ORDER BY cash_conversion_cycle
    ) AS ccc_rank
FROM retail_financial_info
ORDER BY fiscal_year, ccc_rank;