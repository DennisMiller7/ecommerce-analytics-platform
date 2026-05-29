import pandas as pd
import streamlit as st

st.title("E-Commerce Analytics Dashboard")

top_categories = pd.read_csv("data/processed/analytics/top_categories_by_revenue.csv")
orders_by_state = pd.read_csv("data/processed/analytics/orders_by_state.csv")
monthly_revenue = pd.read_csv("data/processed/analytics/monthly_revenue.csv")

st.subheader("Top 10 Categories by Revenue")
st.dataframe(top_categories)
st.bar_chart(top_categories, x="product_category_name", y="revenue")

st.subheader("Orders by Customer State")
st.dataframe(orders_by_state)
st.bar_chart(orders_by_state, x="customer_state", y="orders")

st.subheader("Monthly Revenue")
st.line_chart(monthly_revenue, x="month", y="revenue")