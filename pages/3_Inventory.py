import streamlit as st
import pandas as pd

st.title("📦 Inventory")

df=pd.read_csv("data/inventory.csv")

st.dataframe(df,use_container_width=True)

low_stock=df[df["Quantity"]<40]

st.subheader("⚠ Low Stock Alerts")

st.dataframe(low_stock)