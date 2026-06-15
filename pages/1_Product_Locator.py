import streamlit as st
import pandas as pd

st.title("📍 Product Locator")

df=pd.read_csv("data/inventory.csv")

search=st.text_input("Search Product")

if search:

    result=df[
        df["Product"].str.contains(
            search,
            case=False
        )
    ]

    if len(result)>0:

        st.success("Product Found")

        st.dataframe(result,use_container_width=True)

    else:
        st.error("Product Not Found")
else:
    st.dataframe(df,use_container_width=True)