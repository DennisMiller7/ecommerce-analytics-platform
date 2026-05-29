import pandas as pd
from pathlib import Path

PROCESSED_PATH = Path("data/processed")

df = pd.read_csv(PROCESSED_PATH / "ecommerce_master_table.csv")

total_revenue = df["price"].sum()
total_orders = df["order_id"].nunique()
avg_order_value = total_revenue / total_orders

print("Total revenue:", round(total_revenue, 2))
print("Total orders:", total_orders)
print("Average order value:", round(avg_order_value, 2))

top_categories = (
    df.groupby("product_category_name")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop categories by revenue:")
print(top_categories)