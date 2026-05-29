import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

OUTPUT_PATH = Path("data/processed/analytics")
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

engine = create_engine(
    "postgresql://postgres:ecommerce2026@localhost:5432/ecommerce"
)

queries = {
    "top_categories_by_revenue": """
        SELECT product_category_name, SUM(price) AS revenue
        FROM ecommerce_orders
        GROUP BY product_category_name
        ORDER BY revenue DESC
        LIMIT 10;
    """,

    "orders_by_state": """
        SELECT customer_state, COUNT(DISTINCT order_id) AS orders
        FROM ecommerce_orders
        GROUP BY customer_state
        ORDER BY orders DESC;
    """,

    "monthly_revenue": """
        SELECT 
            DATE_TRUNC('month', order_purchase_timestamp::timestamp) AS month,
            SUM(price) AS revenue
        FROM ecommerce_orders
        GROUP BY month
        ORDER BY month;
    """
}

for name, query in queries.items():
    df = pd.read_sql(query, engine)
    df.to_csv(OUTPUT_PATH / f"{name}.csv", index=False)
    print(f"Saved {name}.csv")