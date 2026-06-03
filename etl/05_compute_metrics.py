import pandas as pd

# Load datasets
bs = pd.read_csv("data/clean/balancesheet.csv")
pl = pd.read_csv("data/clean/profitandloss.csv")
cf = pd.read_csv("data/clean/cashflow.csv")

# -----------------------------
# Balance Sheet Metrics
# -----------------------------

bs["debt_to_equity"] = (
    bs["borrowings"] /
    (bs["equity_capital"] + bs["reserves"])
)

bs["equity_ratio"] = (
    (bs["equity_capital"] + bs["reserves"])
    / bs["total_assets"]
)

# -----------------------------
# Profitability Metrics
# -----------------------------

pl["net_profit_margin_pct"] = (
    pl["net_profit"] / pl["sales"]
) * 100

pl["expense_ratio_pct"] = (
    pl["expenses"] / pl["sales"]
) * 100

pl["interest_coverage"] = (
    pl["operating_profit"] / pl["interest"]
)

# -----------------------------
# Cash Flow Metrics
# -----------------------------

cf["free_cash_flow"] = (
    cf["operating_activity"] +
    cf["investing_activity"]
)

# Save results
bs.to_csv(
    "data/clean/balancesheet_metrics.csv",
    index=False
)

pl.to_csv(
    "data/clean/profitandloss_metrics.csv",
    index=False
)

cf.to_csv(
    "data/clean/cashflow_metrics.csv",
    index=False
)

print("Metrics calculated successfully.")

print("\nBalance Sheet:")
print(bs[[
    "company_id",
    "year",
    "debt_to_equity",
    "equity_ratio"
]].head())

print("\nProfit & Loss:")
print(pl[[
    "company_id",
    "year",
    "net_profit_margin_pct",
    "expense_ratio_pct",
    "interest_coverage"
]].head())

print("\nCash Flow:")
print(cf[[
    "company_id",
    "year",
    "free_cash_flow"
]].head())