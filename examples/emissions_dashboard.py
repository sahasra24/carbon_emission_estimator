import streamlit as st
import pandas as pd

# ✅ This works when script and CSV are in the same folder
df = pd.read_csv("emissions.csv")

st.title("🌿 Carbon Emissions Dashboard")
st.line_chart(df["emissions"])
st.dataframe(df)
