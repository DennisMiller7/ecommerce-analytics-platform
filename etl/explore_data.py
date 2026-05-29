import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")

files = [
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_products_dataset.csv",
    "olist_customers_dataset.csv"
]

for file in files:
    df = pd.read_csv(RAW_PATH/file)

    print("\n==============================")
    print(file)
    print("Shape:", df.shape)
    print("Columns:", list(df.columns))
    print("Missing values:")
    print(df.isnull().sum())