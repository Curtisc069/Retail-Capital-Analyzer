# Retail-Capital-Analyzer

## Project Overview
Analyzing the Working Capital Efficiency of well known U.S retailer companies using Python, SQL, and Excel

This project analyzes the working capital efficiency of the following five major retailing companies between the years 2021 and 2025:
- Costco
- Walmart
- Target
- Best Buy
- Home Depot

The end goal of this project was to analyze and compare the efficiency of how each of these companies manage their inventories, receivables, payables, and short-term liquidity.

This project required the use of financial statement data extracted from each company's annual reports and applies several working capital metrics including the following:
- Working Capital
- Current Ratio
- Days Inventory Outstanding (DIO)
- Days Payables Outstanding (DPO)
- Days Sales Outstanding (DSO)
- Cash Conversion Cycle (CCC)

--
# Project Tools Used
- Excel: Raw Data Collection, Calculations for Capital Metrics, and Cleaning Data
- PostgreSQL: Data Storage and SQL Analysis on Capital Metrics
- Python:
  - pandas: Data Manipulation and Analysis
  - matplotlib: Data Visualization
- Visual Studio Code: General Source-Code Editor
- GitHub: Project Documentation Platform

## Project Dataset
The dataset contains 25 observations:

- 5 companies
- 5 fiscal years per company
- 2021–2025

Financial values are reported in millions (USD)

The cleaned dataset includes the following:

- company
- ticker
- fiscal_year
- revenue
- cogs (cost of goods sold)
- receivable_accounts
- inventory
- payable_accounts
- current_assets
- current_liabilities
- working_capital
- current_ratio
- dio
- dpo
- dso
- cash_conversion_cycle

---

## Primary Metrics

### Working Capital

Working Capital = Current Assets - Current Liabilities

The working capital measures the short-term liquidity of each company.

### Current Ratio

Current Ratio = Current Assets / Current Liabilities

The current ratio measures the ability of a company to meet its short-term responsibilities.

### Days Inventory Outstanding (DIO)

The DIO estimates how long inventory is held by a company before being sold.

DIO = Average Inventory / COGS × 365

### Days Payables Outstanding (DPO)

The DPO estimates how long a company takes to pay its suppliers after receiving the goods.

DPO = Average Accounts Payable / COGS × 365

### Days Sales Outstanding (DSO)

The DSO estimates how long it takes a company to collect its receivables.

DSO = Average Receivables / Company Revenue × 365

### Cash Conversion Cycle (CCC)

CCC = DSO + DIO - DPO

A lower CCC typically indicates a better working capital efficiency because the company converts its operating cycle back into cash faster, making it more liquid.

## SQL Analysis

SQL was used to analyze:

- The 5-year average CCC by company
- The average DIO, DPO, and DSO
- The year-to-year CCC changes
- The company rankings by CCC within each fiscal year

Example Below:

SELECT
    company,
    ROUND(AVG(cash_conversion_cycle), 2) AS avg_cash_conversion_cycle
FROM retail_financial_info
GROUP BY company
ORDER BY avg_cash_conversion_cycle;
