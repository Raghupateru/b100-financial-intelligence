import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="B100 Financial Intelligence Platform",
    layout="wide"
)

# --------------------------------------------------
# Base Directory
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📊 B100 Financial Intelligence Platform")

st.markdown("""
## End-to-End Financial Intelligence Project

This project demonstrates a complete Financial Analytics pipeline built using Python, PostgreSQL, Power BI, Git, GitHub, and Streamlit.

### Technology Stack

- Python
- Pandas
- PostgreSQL
- Power BI
- Git & GitHub
- Streamlit

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

# --------------------------------------------------
# Dataset Overview
# --------------------------------------------------

st.header("📂 Dataset Overview")

companies = pd.read_csv(
    BASE_DIR / "data" / "clean" / "companies.csv"
)

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Companies", len(companies))

with col2:
    st.metric("Dataset Columns", len(companies.columns))

st.dataframe(companies.head())

st.divider()

# --------------------------------------------------
# ETL Pipeline
# --------------------------------------------------

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

- Debt-to-Equity Ratio
- Equity Ratio
- Net Profit Margin
- Expense Ratio
- Interest Coverage Ratio
- Free Cash Flow
- Return on Equity (ROE)
- Return on Capital Employed (ROCE)
""")

st.divider()

# --------------------------------------------------
# Business Impact
# --------------------------------------------------

st.header("📈 Business Impact")

st.markdown("""
- Analyzed **92 public companies**
- Processed **financial statement datasets**
- Built an **end-to-end ETL pipeline**
- Created **financial KPI calculations**
- Designed a **PostgreSQL data warehouse**
- Developed **Power BI dashboards**
- Deployed a **live analytics application**
""")

st.divider()

# --------------------------------------------------
# Dashboard Screenshots
# --------------------------------------------------

st.header("📊 Dashboard Screenshots")

st.subheader("Executive Dashboard")

st.image(
    BASE_DIR / "screenshots" / "executive_dashboard.png",
    use_container_width=True
)

st.subheader("Financial Health Dashboard")

st.image(
    BASE_DIR / "screenshots" / "financial_health.png",
    use_container_width=True
)

st.subheader("Cash Flow Dashboard")

st.image(
    BASE_DIR / "screenshots" / "cashflow_dashboard.png",
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# Repository
# --------------------------------------------------

st.header("🔗 Project Repository")

st.markdown(
    "[GitHub Repository](https://github.com/Raghupateru/b100-financial-intelligence)"
)

st.success("Financial Intelligence Platform Running Successfully 🚀")