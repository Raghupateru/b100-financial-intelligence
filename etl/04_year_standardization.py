import pandas as pd
import re

def standardize_year(year):

    if pd.isna(year):
        return None

    year = str(year).strip()

    if year == "TTM":
        return "TTM"

    match = re.match(r"([A-Za-z]+)-(\d{2})", year)

    if match:
        month = match.group(1)
        yr = int(match.group(2))

        if yr <= 30:
            full_year = 2000 + yr
        else:
            full_year = 1900 + yr

        return f"{month} {full_year}"

    return year


df = pd.read_csv(
    "data/clean/profitandloss.csv"
)

df["year_standardized"] = df["year"].apply(
    standardize_year
)

print(
    df[["year", "year_standardized"]]
    .drop_duplicates()
    .head(20)
)