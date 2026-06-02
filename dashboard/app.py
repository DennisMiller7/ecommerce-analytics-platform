import pandas as pd
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.title("E-Commerce Analytics Dashboard")

summary = requests.get(f"{API_URL}/summary").json()
top_categories = pd.DataFrame(requests.get(f"{API_URL}/top-categories").json())
monthly_revenue = pd.DataFrame(requests.get(f"{API_URL}/monthly-revenue").json())
orders_by_state = pd.DataFrame(requests.get(f"{API_URL}/orders-by-state").json())

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", round(summary["total_revenue"], 2))
col2.metric("Total Orders", summary["total_orders"])
col3.metric("Average Order Value", round(summary["average_order_value"], 2))

st.subheader("Top Categories by Revenue")
st.bar_chart(top_categories, x="product_category_name", y="revenue")

st.subheader("Monthly Revenue")
st.line_chart(monthly_revenue, x="month", y="revenue")

st.subheader("Orders by State")
st.bar_chart(orders_by_state, x="customer_state", y="orders")