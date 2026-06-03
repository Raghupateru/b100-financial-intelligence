import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres123@localhost:5432/bluestock_dw"
)

print("Connected to PostgreSQL")

# Balance Sheet
bs = pd.read_csv("data/clean/balancesheet.csv")

bs[
    [
        "id",
        "company_id",
        "year",
        "equity_capital",
        "reserves",
        "borrowings",
        "total_assets"
    ]
].to_sql(
    "fact_balance_sheet",
    engine,
    if_exists="append",
    index=False
)

print("fact_balance_sheet loaded")

# Cash Flow
cf = pd.read_csv("data/clean/cashflow.csv")

cf.to_sql(
    "fact_cash_flow",
    engine,
    if_exists="append",
    index=False
)

print("fact_cash_flow loaded")

# Analysis
analysis = pd.read_csv("data/clean/analysis.csv")

analysis.to_sql(
    "fact_analysis",
    engine,
    if_exists="append",
    index=False
)

print("fact_analysis loaded")

# Pros & Cons
pc = pd.read_csv("data/clean/prosandcons.csv")

pc.to_sql(
    "fact_pros_cons",
    engine,
    if_exists="append",
    index=False
)

print("fact_pros_cons loaded")