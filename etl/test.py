import pandas as pd

companies = pd.read_excel(
    "data/raw/companies.xlsx",
    header=1
)

print(companies.head())
print("\nRows:", len(companies))
print("\nColumns:")
print(companies.columns.tolist())