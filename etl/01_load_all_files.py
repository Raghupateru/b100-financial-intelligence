import pandas as pd

files = [
    "companies.xlsx",
    "analysis.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "profitandloss.xlsx",
    "documents.xlsx",
    "prosandcons.xlsx"
]

for file in files:
    print("\n" + "=" * 60)
    print("FILE:", file)

    df = pd.read_excel(
        f"data/raw/{file}",
        header=None
    )

    print(df.head(5))
    print("Shape:", df.shape)