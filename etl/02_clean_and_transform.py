import pandas as pd
from pathlib import Path

RAW_PATH = "data/raw"
CLEAN_PATH = "data/clean"

Path(CLEAN_PATH).mkdir(parents=True, exist_ok=True)

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

    print(f"\nProcessing {file}...")

    df = pd.read_excel(
        f"{RAW_PATH}/{file}.xlsx",
        header=1
    )

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Trim spaces from column names
    df.columns = [str(col).strip() for col in df.columns]

    # Replace NULL strings
    df = df.replace(
        ["NULL", "Null", "null"],
        pd.NA
    )

    # Save clean version
    output_file = f"{CLEAN_PATH}/{file}.csv"

    df.to_csv(
        output_file,
        index=False
    )

    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Saved:", output_file)

print("\nAll datasets cleaned successfully.")