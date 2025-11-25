
import pandas as pd
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

RAW_FILE = os.path.join(DATA_DIR, "raw_sales.csv")

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

print("🔄 Loading raw sales data...")
df = pd.read_csv(RAW_FILE)

# ---- Basic Cleaning ----
print("🧹 Cleaning data...")

# Standardize column names (lowercase, no spaces)
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# Convert dates
date_cols = ["order_date", "ship_date"]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Drop rows with missing essential fields
df = df.dropna(subset=["order_id", "order_date", "customer_id", "product_id", "sales"])

# Fill missing text fields with "Unknown"
text_cols = ["customer_name", "segment", "country", "region", "state", "city",
             "product_name", "category", "sub_category"]
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")

# Ensure numeric columns
num_cols = ["sales", "quantity", "discount", "profit"]
for col in num_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

print("✅ Basic cleaning done.")

# ---- Dimension Tables ----

print("📅 Creating dim_date...")
# dim_date from order_date
date_df = pd.DataFrame(df["order_date"].dropna().unique(), columns=["date"])
date_df["date_key"] = date_df["date"].dt.strftime("%Y%m%d").astype(int)
date_df["year"] = date_df["date"].dt.year
date_df["month"] = date_df["date"].dt.month
date_df["month_name"] = date_df["date"].dt.strftime("%b")
date_df["quarter"] = date_df["date"].dt.quarter

dim_date = date_df[["date_key", "date", "year", "month", "month_name", "quarter"]]
dim_date.to_csv(os.path.join(OUTPUT_DIR, "dim_date.csv"), index=False)
print("✅ dim_date.csv created.")

print("👤 Creating dim_customer...")
dim_customer = (
    df[["customer_id", "customer_name", "segment", "country", "region", "state", "city"]]
    .drop_duplicates()
    .reset_index(drop=True)
)
dim_customer.to_csv(os.path.join(OUTPUT_DIR, "dim_customer.csv"), index=False)
print("✅ dim_customer.csv created.")

print("📦 Creating dim_product...")
dim_product = (
    df[["product_id", "product_name", "category", "sub_category"]]
    .drop_duplicates()
    .reset_index(drop=True)
)
dim_product.to_csv(os.path.join(OUTPUT_DIR, "dim_product.csv"), index=False)
print("✅ dim_product.csv created.")

# ---- Fact Table ----

print("📊 Creating fact_sales...")
df["order_date_key"] = df["order_date"].dt.strftime("%Y%m%d").astype(int)

fact_sales = df[
    [
        "order_id",
        "order_date_key",
        "customer_id",
        "product_id",
        "sales",
        "quantity",
        "discount",
        "profit",
        "country",
        "region",
        "state",
        "city",
    ]
].copy()

fact_sales.to_csv(os.path.join(OUTPUT_DIR, "fact_sales.csv"), index=False)
print("✅ fact_sales.csv created.")

print("🎉 ETL pipeline completed successfully. Files saved in 'output/' folder.")
