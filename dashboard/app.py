import pandas as pd
import streamlit as st
import requests

st.title("E-Commerce Analytics Dashboard")

response = requests.get("http://127.0.0.1:8000/top-categories")
data = response.json()

top_categories = pd.DataFrame(data)

st.subheader("Top 10 Categories by Revenue")
st.dataframe(top_categories)
st.bar_chart(top_categories, x="product_category_name", y="revenue")