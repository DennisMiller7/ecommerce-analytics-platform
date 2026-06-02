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

@app.get("/summary")
def summary():

    query = """
    SELECT
        SUM(price) AS total_revenue,
        COUNT(DISTINCT order_id) AS total_orders,
        SUM(price) / COUNT(DISTINCT order_id) AS average_order_value
    FROM ecommerce_orders;
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")[0]

@app.get("/monthly-revenue")
def monthly_revenue():

    query = """
    SELECT
        TO_CHAR(
            DATE_TRUNC('month', order_purchase_timestamp::timestamp),
            'YYYY-MM'
        ) AS month,
        COALESCE(SUM(price), 0) AS revenue
    FROM ecommerce_orders
    WHERE order_purchase_timestamp IS NOT NULL
    GROUP BY month
    ORDER BY month;
    """

    df = pd.read_sql(query, engine)
    print(df[df["revenue"].isna()])

    df = df.fillna(0)

    return df.to_dict(orient="records")

@app.get("/orders-by-state")
def orders_by_state():

    query = """
    SELECT
        customer_state,
        COUNT(DISTINCT order_id) AS orders
    FROM ecommerce_orders
    GROUP BY customer_state
    ORDER BY orders DESC;
    """

    df = pd.read_sql(query, engine)

    return df.to_dict(orient="records")