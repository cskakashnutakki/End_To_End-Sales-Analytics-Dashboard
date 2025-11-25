
# Sales Analytics Dashboard Starter Project

This folder contains:
- `data/raw_sales.csv` → synthetic sample sales dataset
- `etl_sales_pipeline.py` → Python ETL script that creates star-schema CSVs for Power BI in the `output/` folder

## How to run ETL

1. Install Python and pandas:
   ```bash
   pip install pandas
   ```
2. Run the ETL script from this folder:
   ```bash
   python etl_sales_pipeline.py
   ```
3. Open Power BI Desktop and load the CSV files from the `output/` folder.
