import pandas as pd
import os

files = [
    "companies",
    "analysis",
    "balancesheet",
    "cashflow",
    "profitandloss",
    "documents",
    "prosandcons"
]

for file in files:

    print("\n" + "=" * 70)
    print(f"TABLE: {file.upper()}")

    df = pd.read_csv(f"data/clean/{file}.csv")

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    if "company_id" in df.columns:
        print("\nUnique Companies:")
        print(df["company_id"].nunique())

    if "year" in df.columns:
        print("\nSample Years:")
        print(df["year"].dropna().unique()[:15])