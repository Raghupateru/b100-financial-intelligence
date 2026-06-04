import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
page_title="B100 Financial Intelligence Platform",
layout="wide"
)

st.title("📊 B100 Financial Intelligence Platform")

st.markdown("""

## End-to-End Financial Intelligence Project

This project demonstrates a complete Financial Analytics pipeline built using Python, PostgreSQL, Power BI, Git, and Streamlit.

### Technology Stack

* Python
* Pandas
* PostgreSQL
* Power BI
* Git & GitHub
* Streamlit

### Project Workflow

Raw Financial Data
⬇
Data Cleaning & Transformation
⬇
Feature Engineering & KPI Calculation
⬇
PostgreSQL Data Warehouse
⬇
Power BI Dashboard Development
⬇
Interactive Reporting & Visualization
""")

st.divider()

# Dataset Overview

st.header("📂 Dataset Overview")

companies = pd.read_csv("../data/clean/companies.csv")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Companies", len(companies))

with col2:
    st.metric("Dataset Columns", len(companies.columns))

st.dataframe(companies.head())

st.divider()

# ETL Overview

st.header("⚙️ ETL Pipeline")

st.markdown("""

### ETL Components

1. Data Loading
2. Data Cleaning
3. Data Profiling
4. Year Standardization
5. Financial KPI Computation
6. PostgreSQL Warehouse Loading
7. Power BI Dashboard Creation

### Financial Metrics Calculated

* Debt to Equity Ratio
* Equity Ratio
* Net Profit Margin
* Expense Ratio
* Interest Coverage Ratio
* Free Cash Flow
* ROE
* ROCE
  """)

st.divider()

# Dashboard Screenshots

st.header("📈 Dashboard Screenshots")

st.subheader("Executive Dashboard")
st.image("../screenshots/executive_dashboard.png")

st.subheader("Financial Health Dashboard")
st.image("../screenshots/financial_health.png")

st.subheader("Cash Flow Dashboard")
st.image("../screenshots/cashflow_dashboard.png")

st.divider()

st.header("🔗 Project Repository")

st.markdown(
"[GitHub Repository](https://github.com/Raghupateru/b100-financial-intelligence)"
)

st.success("Financial Intelligence Platform Running Successfully")
