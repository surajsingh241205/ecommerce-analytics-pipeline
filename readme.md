# Olist E-Commerce Data Analytics Project

An end-to-end e-commerce analytics project built using **Python, SQL, PostgreSQL (Neon), Power BI, and GitHub Actions** to transform raw Brazilian e-commerce data into meaningful business insights.

The project covers the complete data analytics lifecycle — from data cleaning and exploratory data analysis to database engineering, SQL analytics, Python analysis, automated data validation, and interactive business intelligence dashboards.

---

## Project Overview

The objective of this project is to analyze Olist's historical e-commerce data and understand business performance across sales, customers, products, sellers, payments, and delivery operations.

The analysis focuses on answering important business questions:

- How is revenue performing over time?
- Which product categories generate the most revenue?
- How frequently do customers make repeat purchases?
- How does customer retention change across acquisition cohorts?
- Which products and sellers contribute most to business performance?
- Which payment methods contribute the most revenue?
- How do delivery delays relate to customer satisfaction?

### Project Highlights

| Metric | Result |
|---|---:|
| Total Revenue | R$15.42 Million |
| Total Orders | 96.48K |
| Average Order Value | R$159.86 |
| Total Customers | 93K |
| Total Products | 32K |
| Total Sellers | 3K |
| Product Categories | 74 |
| Units Sold | 110.20K |
| Cleaned Dataset Records | 1.39 Million |
| Analytical SQL Tables | 8 |
| Power BI Dashboard Pages | 4 |

**Data period:** 2016–2018  
**Currency:** Brazilian Real (BRL)

---

## Dashboard Preview

The Power BI report contains four interactive pages designed to provide different perspectives on business performance.

### 1. Executive Overview

![Executive Overview](images/executive-overview.png)

Key metrics:
- Total Revenue
- Total Orders
- Average Order Value
- Total Customers

Visualizations:
- Monthly Revenue Trend
- Monthly Orders
- Top 10 Categories by Revenue
- Average Order Value Trend

### 2. Customer Insights

![Customer Insights](images/customer-insights.png)

Key metrics:
- Repeat Customers
- Average Customer Lifetime Value
- One-Time Customers

Visualizations:
- Customer Cohort Retention Analysis
- Customer Lifetime Value Distribution
- Customer Purchase Frequency

### 3. Products & Sellers

![Products and Sellers](images/products-sellers.png)

Key metrics:
- Total Products
- Total Sellers
- Product Revenue
- Units Sold
- Total Categories

Visualizations:
- Top 10 Products by Revenue
- Category Revenue Performance
- Category Orders vs Units Sold
- Top 10 Products by Units Sold

### 4. Operations & Delivery Performance

![Operations and Delivery](images/operations-delivery.png)

Key metrics:
- Delivered Orders
- Late Deliveries
- Late Delivery Rate
- Average Delivery Days
- Average Review Score

Visualizations:
- Payment Method Distribution
- Monthly Late Delivery Rate
- Monthly Customer Review Score
- Monthly Negative Review Rate

**Live Power BI Report:**  
[View Interactive Dashboard](https://app.powerbi.com/groups/me/reports/a7d6697b-f0da-4f5f-ac6f-76c6863c332c/adf2a8f2286a9b8d3ad6?experience=power-bi)

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data cleaning, EDA, analysis, and database extraction |
| Pandas | Data manipulation and transformation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook | Exploratory analysis and documentation |
| PostgreSQL | Relational database and analytical storage |
| Neon | Cloud-hosted PostgreSQL database |
| SQL | Data aggregation, joins, CTEs, and analytical queries |
| Power BI Desktop | Interactive dashboard development |
| Power BI Service | Publishing and sharing dashboards |
| Git & GitHub | Version control and project management |
| GitHub Actions | Automated workflow execution |
| Pytest | Data and database validation |

---

## End-to-End Data Workflow

The project follows a structured analytics pipeline.

### Step 1: Data Sources

The project uses the historical Olist Brazilian E-Commerce public dataset.

The dataset contains nine CSV files:

1. Customers
2. Geolocation
3. Orders
4. Order Items
5. Order Payments
6. Order Reviews
7. Products
8. Sellers
9. Product Category Translation

These datasets contain information about customer transactions, product details, payments, sellers, reviews, and delivery operations.

### Step 2: Data Cleaning & Exploratory Data Analysis

**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook

Performed:
- Inspected dataset structures and data types.
- Identified and removed exact duplicate rows.
- Checked missing values and investigated their context.
- Standardized data types.
- Handled ZIP code formatting.
- Examined timestamp columns and inconsistencies.
- Performed exploratory data analysis.
- Investigated outliers and unusual records.
- Generated statistical summaries and visualizations.

**Final cleaned dataset:**

- 9 processed CSV files.
- 1,395,091 total records.
- No exact duplicate rows remaining in the cleaned files.

Missing values that represented legitimate unavailable information were retained rather than automatically deleted.

### Step 3: PostgreSQL Database Integration

**Tools:** PostgreSQL, Neon, SQLAlchemy, Psycopg2

Loaded all nine processed datasets into the Neon PostgreSQL database under the `staging` schema.

Database structure:

- `staging` — cleaned source datasets.
- `analytics` — business-ready analytical tables.

Validated database row counts against the processed CSV files to ensure successful ingestion.

### Step 4: SQL Analytics & Business Transformation

**Tool:** PostgreSQL SQL

Created eight analytical tables using SQL queries, aggregations, joins, and business logic.

| Analytical Table | Purpose |
|---|---|
| `monthly_sales` | Monthly revenue, orders, and sales performance |
| `customer_analytics` | Customer purchase behavior and lifetime value |
| `customer_retention` | Customer cohort and retention analysis |
| `product_performance` | Product-level revenue and units sold |
| `category_performance` | Category-level business performance |
| `seller_performance` | Seller revenue and order performance |
| `payment_analytics` | Payment methods and payment distribution |
| `delivery_review_analytics` | Delivery performance and customer reviews |

Special attention was given to joining datasets at the correct level of detail to avoid duplicated revenue and misleading aggregations.

### Step 5: Python Analytics

**Tools:** Python, Pandas, Matplotlib, Seaborn, PostgreSQL

Connected Python to Neon PostgreSQL and extracted all eight analytical tables.

Performed deeper analysis on:

- Sales trends and average order value.
- Customer purchase frequency.
- Customer lifetime value distribution.
- Customer cohort retention.
- Product and category performance.
- Seller performance.
- Payment method distribution.
- Delivery performance and customer reviews.

Created visualizations to identify patterns, trends, and potential business improvement areas.

### Step 6: Automated Data Validation

**Tools:** GitHub Actions, Pytest, Python

Implemented automated validation tests to check:

- Processed CSV files exist and are not empty.
- Required columns are available.
- Exact duplicate rows are absent.
- Neon PostgreSQL connection is successful.
- Expected staging tables exist.
- Staging tables contain records.

Configured GitHub Actions to run validation on pushes, pull requests, and manual workflow dispatches.

### Step 7: Power BI Dashboard Development

**Tools:** Power BI Desktop, Power BI Service

Connected Power BI to Neon PostgreSQL and imported the eight analytical tables.

Created a structured data model, calendar table, DAX measures, KPI cards, charts, and four dashboard pages.

Published the completed report to Power BI Service.

---

## Business Insights & Findings

The following findings are based on the analysis and visualizations presented in the Power BI dashboard.

### 1. Executive Overview

**Revenue and sales performance**

- Generated approximately **R$15.42 million in total revenue**.
- Recorded approximately **96.48K orders**.
- Overall Average Order Value was **R$159.86**.
- November 2017 was the strongest month, generating approximately **R$1.15 million** in revenue.
- The monthly revenue trend shows substantial growth during 2017, followed by relatively high monthly revenue levels through much of 2018.

**Category performance**

The leading revenue-generating categories included:

1. Health & Beauty
2. Watches & Gifts
3. Bed, Bath & Table
4. Sports & Leisure
5. Computers & Accessories

Health & Beauty generated approximately **R$1.23 million**, making it the leading category by revenue in the underlying category analysis.

**Business interpretation:** These categories represent important contributors to overall sales performance and may deserve attention when planning product assortment and marketing campaigns.

### 2. Customer Insights

**Customer purchase behavior**

- Approximately **93K one-time customers** are displayed in the dashboard.
- Approximately **3K repeat customers** are displayed.
- Average Customer Lifetime Value: **R$165.20**.

The purchase frequency chart shows a strong concentration of customers with only one order.

**Customer retention**

The cohort retention matrix shows:

- Every cohort starts at 100% in its acquisition month.
- Retention drops sharply after the first purchase.
- Subsequent-month retention percentages are generally very low.
- Later cohorts have fewer observable months because the dataset ends in August 2018.

**Customer Lifetime Value**

The LTV distribution is concentrated in the lower-value ranges, with a smaller number of customers contributing higher lifetime value.

**Business interpretation:** Customer retention is an important area for further investigation. Loyalty programs, personalized offers, post-purchase communication, and repeat-purchase campaigns could be explored to improve customer engagement.

### 3. Products & Sellers

**Product performance**

- Approximately **32K products** are included in the dashboard.
- Product revenue is displayed at approximately **R$13 million**.
- Total units sold: **110.20K**.
- Total categories: **74**.

**Category performance**

Health & Beauty and Watches & Gifts are among the leading categories by revenue.

Bed, Bath & Table leads the displayed category comparison in order volume and units sold.

**Product performance**

The dashboard separately compares the top 10 products by revenue and the top 10 products by units sold.

This highlights an important distinction: products with the highest sales volume are not necessarily the products generating the highest revenue.

**Seller performance**

Approximately 3K sellers are represented in the dashboard.

The underlying analysis also showed that the seller with the highest revenue was not the seller with the highest order volume.

**Business interpretation:** Revenue, order volume, and units sold should be evaluated separately when comparing product and seller performance. High-volume products and high-revenue products may require different inventory and pricing strategies.

### 4. Operations & Delivery Performance

**Delivery performance**

- Delivered Orders: approximately **96K**.
- Late Deliveries: approximately **8K**.
- Late Delivery Rate: **8.1%**.
- Average Delivery Time: **12.56 days**.
- Average Customer Review Score: **4.16 / 5**.

**Payment analysis**

The payment method distribution shows:

| Payment Method | Revenue Share |
|---|---:|
| Credit Card | 78.46% |
| Boleto | 17.96% |
| Voucher | 2.22% |
| Debit Card | 1.35% |

Credit cards account for the largest share of payment value, contributing approximately **R$12.10 million**.

**Customer satisfaction**

The monthly customer review score chart shows a decline around early 2018, reaching approximately **3.8** before recovering.

The monthly negative review rate also varies across the reporting period.

The underlying Python analysis identified a strong negative correlation of approximately **-0.744** between monthly late delivery rates and average review scores across 21 monthly observations.

This indicates an association between higher late delivery rates and lower average review scores. It does not establish causation.

**Business interpretation:** Delivery reliability is an important operational area to investigate when looking for opportunities to improve customer satisfaction.

---

## Challenges Faced & Solutions

Building this project involved several practical data engineering and analytics challenges.

### 1. Handling Large Datasets

**Challenge:** The project contained more than 1.39 million records across nine datasets.

**Solution:** Used Pandas for structured data cleaning and SQLAlchemy with chunked database loading to transfer processed data into PostgreSQL.

### 2. Managing Missing Values and Data Quality

**Challenge:** Several datasets contained missing values, timestamp gaps, and unusual records.

**Solution:** Investigated missing values and retained legitimate unavailable information instead of deleting records without business justification. Added automated checks for duplicate records, required columns, and empty datasets.

### 3. Avoiding Duplicate Revenue Calculations

**Challenge:** An order can contain multiple items and multiple payment records. Directly joining these tables can multiply rows and inflate revenue.

**Solution:** Aggregated payment records at the order level before joining them to other datasets used for sales analysis.

### 4. Working With Different Data Granularities

**Challenge:** Analytical tables represented different levels of detail, including monthly sales, individual customers, products, categories, and sellers.

**Solution:** Designed separate analytical tables and avoided relationships between incompatible aggregated tables in Power BI.

### 5. Customer Retention Analysis

**Challenge:** Cohort analysis requires tracking customers across multiple months. Future months for recent cohorts cannot be treated as zero retention because those months are not yet observable.

**Solution:** Built a cohort retention matrix and represented unobserved future periods as blank values.

### 6. Accurate KPI Calculations

**Challenge:** Calculating averages from already aggregated data can produce misleading results if the underlying record counts are ignored.

**Solution:** Used weighted-average calculations for delivery duration and customer review scores, with the relevant order counts as weights.

### 7. Database and Automation Integration

**Challenge:** Connecting local Python scripts and GitHub Actions to a cloud-hosted PostgreSQL database required environment configuration and secure credential handling.

**Solution:** Used environment variables and GitHub repository secrets for database configuration, along with automated connection and staging-table validation tests.

---

## Project Architecture

The complete workflow can be summarized as:

```text
Olist Historical E-Commerce Dataset
                 |
                 v
        Python Data Processing
          Pandas | NumPy
                 |
                 v
       Cleaning & Exploratory Analysis
                 |
                 v
       Processed CSV Datasets
                 |
                 v
       Neon PostgreSQL Database
                 |
           +-----+-----+
           |           |
           v           v
        Staging     SQL Analytics
        Tables      & Aggregations
                        |
                        v
                8 Analytical Tables
                        |
                        v
                 Python Analytics
                        |
                        v
                 Power BI Desktop
                        |
                        v
                 4-Page Dashboard
                        |
                        v
                 Power BI Service
```

**Automation and validation:** GitHub Actions and Pytest validate processed datasets, database connectivity, and staging tables.

---

## Repository Structure

```text
ecommerce-analytics-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── ingestion/
│   └── load_to_postgres.py
│
├── notebooks/
│   └── python_analytics.ipynb
│
├── tests/
│   ├── test_processed_data.py
│   ├── test_database_connection.py
│   └── test_staging_tables.py
│
├── .github/
│   └── workflows/
│       └── data-validation.yml
│
├── .gitignore
├── requirements.txt
└── README.md
```

*The structure above highlights the main project components; additional files and folders may exist in the repository.*

---

## Key Technical Concepts Applied

Throughout this project, I worked with:

**Python**
- Data manipulation using Pandas.
- Numerical operations using NumPy.
- Exploratory Data Analysis.
- Statistical analysis and visualization.
- Database connectivity using SQLAlchemy.

**SQL**
- Joins and aggregations.
- Common Table Expressions (CTEs).
- Subqueries.
- Window functions.
- Date-based analysis.
- Business metric calculations.
- Analytical table creation.

**Power BI**
- Data modeling.
- Calendar table creation.
- DAX measures.
- KPI cards.
- Time-series analysis.
- Cohort retention matrix.
- Conditional formatting.
- Interactive report design.

**Automation**
- Git version control.
- GitHub Actions workflows.
- Pytest-based validation.
- Environment variables and repository secrets.

---

## Limitations & Scope

- The project uses historical Olist data covering 2016–2018; it is not a live e-commerce data feed.
- GitHub Actions performs scheduled or event-triggered validation when configured; it does not make the historical dataset real-time.
- The analysis describes patterns in the available data and should not be interpreted as proof of causation.
- Product, customer, and seller identifiers are used where descriptive names are not available in the analytical dataset.
- Dashboard values are rounded for presentation.

---

## What I Learned

This project helped me understand how different components of a real-world analytics workflow work together.

Key learning outcomes:

- Building an end-to-end data analytics pipeline.
- Cleaning and validating large datasets.
- Connecting Python applications to cloud PostgreSQL databases.
- Designing analytical tables using SQL.
- Performing business-focused exploratory analysis.
- Understanding customer retention and cohort analysis.
- Creating weighted business metrics.
- Building multi-page Power BI dashboards.
- Automating data validation with GitHub Actions.
- Documenting and maintaining a project using GitHub.

---

## Project Links

**Power BI Dashboard:**  
https://app.powerbi.com/groups/me/reports/a7d6697b-f0da-4f5f-ac6f-76c6863c332c/adf2a8f2286a9b8d3ad6?experience=power-bi

**LinkedIn:**  
https://www.linkedin.com/in/suraj-singh-data-science/

---

## Author

**Suraj Kumar Singh**  
Aspiring Data Analyst | Python | SQL | PostgreSQL | Power BI

I am continuously learning and building practical projects to strengthen my skills in data analytics, data visualization, and business intelligence.

If you find this project useful, feel free to explore the repository, share your feedback, and connect with me on LinkedIn.

**Thank you for visiting!**