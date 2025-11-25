
# End-to-End Sales Analytics Dashboard (Power BI + SQL + Python)

An end-to-end Business Intelligence project that automates the sales reporting process using **Python, SQL, and Power BI**.  
This project covers the complete data lifecycle: **data extraction → cleaning → modeling → ETL → visualization → insights.**

---

## 🚀 Project Overview

The goal of this project is to help business stakeholders track and analyze sales performance across:
- Regions
- Product categories
- Customer segments
- Time periods (Year, Quarter, Month)

Key features:
- Python-based ETL pipeline to clean and transform raw sales data
- Star schema data model (Fact & Dimension tables)
- Power BI interactive dashboard with key business KPIs
- YoY growth analysis and demand trends

---

## 🚀 Project Preview

<img width="957" height="540" alt="image" src="https://github.com/user-attachments/assets/69d2c2dc-ab6a-4712-9366-c2384b54f6cc" />

<img width="583" height="340" alt="image" src="https://github.com/user-attachments/assets/83f649a2-d938-4915-83bf-0569a7240040" />

<img width="958" height="540" alt="image" src="https://github.com/user-attachments/assets/e48c3318-5a89-43b1-93ce-eb124476c468" />

---

## 🧱 Tech Stack

- **Language**: Python
- **Libraries**: Pandas
- **Database**: (Optional) SQL / MySQL / SQL Server
- **Visualization**: Power BI
- **Data Modeling**: Star schema (Fact + Dimensions)
- **Other**: DAX (for measures and KPIs)

---

## 📁 Project Structure

```text
Sales-Analytics-Dashboard/
 ├── data/
 │    └── raw_sales.csv
 ├── output/
 │    ├── dim_date.csv
 │    ├── dim_customer.csv
 │    ├── dim_product.csv
 │    └── fact_sales.csv
 ├── etl_sales_pipeline.py
 └── README.md
```
📊 Dataset

The raw dataset (data/raw_sales.csv) contains transactional-level sales data with columns like:
```
• order_id

• order_date

• ship_date

• customer_id, customer_name, segment

• country, region, state, city

• product_id, product_name, category, sub_category

• sales, quantity, discount, profit
```
You can use any retail/e-commerce sales dataset (e.g., Superstore dataset) and align the column names accordingly.

🔄 ETL Pipeline (Python)

File: etl_sales_pipeline.py

Main steps:

1. Load raw sales data from raw_sales.csv

2. Clean and standardize columns (types, missing values, formats)

3. Create:
```
  • dim_date (date-level features: year, month, quarter, etc.)

  • dim_customer (customer attributes)

  • dim_product (product attributes)

  • fact_sales (fact table with keys and numeric metrics)
```
4. Export cleaned tables as CSV files into the output/ folder for Power BI.

🧠 Data Model (Star Schema)

The data model follows a star schema:

• Fact Table
```
  • fact_sales
```
• Dimension Tables
```
  • dim_date

  • dim_customer

  • dim_product
```
• Relationships in Power BI:
```
  • fact_sales[order_date_key] → dim_date[date_key]

  • fact_sales[customer_id] → dim_customer[customer_id]

  • fact_sales[product_id] → dim_product[product_id]   
```
📈 Power BI Dashboard

The Power BI report includes:

• KPI Cards
```
  • Total Sales

  • Total Profit

  • Profit Margin %

  • Total Quantity Sold
```
• Visuals
```
  • Sales by Region (Bar/Column chart)

  • Sales by Product Category & Sub-Category (Stacked column chart)

  • Monthly Sales Trend (Line chart by Year/Month)

  • Top 10 Products by Sales (Bar chart)

  • Sales by Customer Segment (Pie/Donut chart)
```
• Filters / Slicers
```
  • Year

  • Region

  • Category

  • Segment  
```
📐 Key DAX Measures

Some of the measures used:
```
Total Sales = SUM(fact_sales[sales])

Total Profit = SUM(fact_sales[profit])

Profit Margin % =
DIVIDE([Total Profit], [Total Sales])

Sales LY =
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(dim_date[date])
)

YoY Sales Growth % =
VAR CurrentSales = [Total Sales]
VAR LastYearSales = [Sales LY]
RETURN
DIVIDE(CurrentSales - LastYearSales, LastYearSales)
```
✅ Key Outcomes

• Automated the sales reporting process via Python ETL and Power BI.

• Improved data quality and consistency using a standardized star schema.

• Provided business users with interactive insights on sales performance and trends.

👤 Author

  • Name: Nutakki Chandra Sekhara Krishna Akash

  • Role: Associate Software Engineer – Data & Analytics (aspiring)

  • LinkedIn: https://www.linkedin.com/in/akash-nutakki/

  • Email: akash.n4243@gmail.com
