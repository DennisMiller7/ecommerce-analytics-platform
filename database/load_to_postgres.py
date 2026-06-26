import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(
    "data/processed/ecommerce_master_table.csv"
)

engine = create_engine(
    "postgresql://postgres:postgres123@localhost:5433/ecommerce"
)

df.to_sql(
    "ecommerce_orders",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully!")