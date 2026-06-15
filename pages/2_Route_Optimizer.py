import streamlit as st

st.title("🛣 Route Optimizer")

products=[
"Wireless Headphones",
"Smart Watch",
"Gaming Mouse",
"Mechanical Keyboard",
"Laptop Backpack",
"Portable Speaker"
]

selected=st.multiselect(
"Select Products To Pick",
products
)

if st.button("Generate Route"):

    st.success("Optimized Picking Route")

    for i,p in enumerate(selected,start=1):
        st.write(f"{i}. {p}")