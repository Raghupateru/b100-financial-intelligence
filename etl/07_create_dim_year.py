import pandas as pd
from sqlalchemy import create_engine

profit = pd.read_csv("data/clean/profitandloss.csv")
balance = pd.read_csv("data/clean/balancesheet.csv")
cash = pd.read_csv("data/clean/cashflow.csv")

years = sorted(
    set(profit["year"].dropna().astype(str))
    | set(balance["year"].dropna().astype(str))
    | set(cash["year"].dropna().astype(str))
)

dim_year = pd.DataFrame({"year_label": years})

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres123@localhost:5432/bluestock_dw"
)

dim_year.to_sql(
    "dim_year",
    engine,
    if_exists="replace",
    index=False
)

print(f"Loaded {len(dim_year)} years")