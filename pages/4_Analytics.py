import streamlit as st
import plotly.express as px
import pandas as pd

st.title("📊 Warehouse Analytics")

data={
"Metric":["Accuracy","Efficiency","Order Completion"],
"Value":[96,88,91]
}

df=pd.DataFrame(data)

fig=px.bar(
    df,
    x="Metric",
    y="Value"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.metric(
    "Average Picking Time",
    "4.2 min"
)