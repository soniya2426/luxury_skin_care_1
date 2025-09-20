import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Luxury Skincare Dashboard", layout="wide")
DATA_FILE = "ibr final responses for dashboard 2.xlsx"

st.title("Luxury Skincare Presentation Dashboard")

@st.cache_data
def load_sheets(path):
    xls = pd.ExcelFile(path, engine="openpyxl")
    return {s: pd.read_excel(path, sheet_name=s, engine="openpyxl") for s in xls.sheet_names}

try:
    sheets = load_sheets(DATA_FILE)
    st.success(f"Loaded {len(sheets)} sheets: {list(sheets.keys())}")
    for name, df in sheets.items():
        st.subheader(f"Sheet: {name}")
        st.write(df.head())
        if df.select_dtypes(include='number').shape[1] >= 2:
            st.plotly_chart(px.scatter(df, x=df.select_dtypes(include='number').columns[0],
                                       y=df.select_dtypes(include='number').columns[1]), use_container_width=True)
except Exception as e:
    st.error(f"Could not load Excel file: {e}")
