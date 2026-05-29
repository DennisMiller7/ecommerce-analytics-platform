import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

orders = pd.read_csv(RAW_PATH / "olist_orders_dataset.csv")
items = pd.read_csv(RAW_PATH / "olist_order_items_dataset.csv")
products = pd.read_csv(RAW_PATH / "olist_products_dataset.csv")
customers = pd.read_csv(RAW_PATH / "olist_customers_dataset.csv")

df = orders.merge(customers, on="customer_id", how="left")
df = df.merge(items, on="order_id", how="left")
df = df.merge(products, on="product_id", how="left")

df = df.drop_duplicates()

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")

PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

df.to_csv(PROCESSED_PATH / "ecommerce_master_table.csv", index=False)

print("Master table created")
print("Shape:", df.shape)
print("Saved to data/processed/ecommerce_master_table.csv")