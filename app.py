import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="WareNav",
    page_icon="📦",
    layout="wide"
)

st.markdown("""
<style>

.main{
background:#F4F7FC;
}

.hero{
background:linear-gradient(90deg,#0f172a,#2563eb);
padding:40px;
border-radius:20px;
color:white;
}

.metric{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0 4px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>📦 WareNav</h1>
<h3>The shortest path to every product.</h3>
<p>Smart Warehouse Navigation & Inventory Management System</p>
</div>
""", unsafe_allow_html=True)

st.write("")

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric("Products",1200)

with col2:
    st.metric("Orders Today",154)

with col3:
    st.metric("Inventory Accuracy","96%")

with col4:
    st.metric("Picking Efficiency","+32%")

st.divider()

st.subheader("Project Overview")

st.info("""
WareNav helps warehouse employees locate products faster,
optimize picking routes, verify bins through QR scanning,
and track inventory in real-time.
""")

st.subheader("Key Features")

c1,c2,c3=st.columns(3)

with c1:
    st.success("📍 Product Locator")

with c2:
    st.success("🛣 Route Optimizer")

with c3:
    st.success("📦 Inventory Tracking")

c4,c5,c6=st.columns(3)

with c4:
    st.success("🔍 QR Verification")

with c5:
    st.success("📊 Analytics")

with c6:
    st.success("🤖 AI Support")