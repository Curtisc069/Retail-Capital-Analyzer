# Retail Capital Analyzer

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

---

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

---

## SQL Analysis

SQL was used to analyze:

- The 5-year average CCC by company
- The average DIO, DPO, and DSO
- The year-to-year CCC changes
- The company rankings by CCC within each fiscal year

## Use of Python

Python was used to:

- Load the clean CSV into a pandas dataframe
- Calculate the average DIO, DPO, and DSO and grouping the data by company
- Comparing the working capital performances across all companies
- Create data visualizations of project findings with matplotlib
  - Comparing the CCC trends from 2021-2025 by company (Line Chart)
  - Comparing the average DIO, DPO, and DSO by company (Bar Graph)
  - Comparing the CCC of each company in 2025 (Bar Graph)
 
## Key Findings
1. Home Depot had the highest Cash Conversion Cycle 
Home Depot had an average CCC of approximately 42 days, significantly higher than the other companies in the dataset. This outcome is mainly due to its relatively high DIO, meaning inventory remained in the operating cycle for longer periods of time compared to the other companies.

2. Target maintained the lowest average Cash Conversion Cycle throughout 2021-2025

Target had the lowest average CCC in the peer group indicating a very strong working capital efficiency compared to the other companies. This may have been due to how high Target's DPO (59 days avg) was compared to its DIO
(63 days avg). Target's DSO was also especially low meaning that Target could often sell inventory and receive customer income before needing to pay their suppliers for that inventory.

Its relatively high DPO helped offset its inventory holding period, meaning the company often collected cash before fully paying suppliers.

3. Costco showed consistently strong working capital efficiency

Costco maintained a very low CCC throughout the five-year period.

Its inventory turnover and supplier payment timing resulted in a short operating cash cycle.

4. Best Buy's CCC increased over time

Best Buy's CCC increased from approximately 1 day in 2021 to over 11 days in 2025.

This suggests a deterioration in working capital efficiency over the period.

5. Walmart remained relatively stable

Walmart maintained a low CCC throughout the period, generally ranging between approximately 1 and 6 days.
