import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres123")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5433")
DB_NAME = os.getenv("DB_NAME", "ecommerce")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

TEST_DATA_PATH = Path("tests/test_data/ecommerce_orders_test.csv")

df = pd.read_csv(TEST_DATA_PATH)

df.to_sql(
    "ecommerce_orders",
    engine,
    if_exists="replace",
    index=False
)

print("Test data loaded successfully")
print("Rows loaded:", len(df))