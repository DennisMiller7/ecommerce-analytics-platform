import os
import pandas as pd
from fastapi import FastAPI
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

@app.get("/")
def root():
    return {"message": "E-Commerce Analytics API"}

@app.get("/top-categories")
def top_categories():
    query = """
    SELECT product_category_name,
           SUM(price) AS revenue
    FROM ecommerce_orders
    GROUP BY product_category_name
    ORDER BY revenue DESC
    LIMIT 10;
    """

    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")