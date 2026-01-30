import pandas as pd
import matplotlib.pyplot as plt

data = {
    "date": [
        "2026-01-01", "2026/01/01", "01-02-2026",
        "2026-01-03", "2026-01-03", None,
        "2026-01-04", "2026-01-05"
    ],
    "category": [
        " food ", "Food", "ENTERTAINMENT",
        "Bills", " bills ", "Transport",
        "transport", "Food"
    ],
    "amount": [
        "12.50", "8.75", "20",
        "120.00", " sixty ", "",
        "7.25", "5.00"
    ],
    "payment_method": [
        "Card", " card ", "CARD",
        "Bank", None, "Cash",
        "cash", "Card"
    ]
}

df = pd.DataFrame(data)

def clean_column(x):
    return x.str.lower().str.title().str.strip()

df = df.rename(columns=lambda x: x.lower())

df["category"] = clean_column(df["category"])

df["payment_method"] = clean_column(df["payment_method"])
df["payment_method"] = df["payment_method"].fillna("Unknown")

df["date"] = pd.to_datetime(df["date"], format="mixed", errors="coerce")

df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

category_summary = df.groupby("category").agg(
    total_spent=("amount", "sum"),
    avg_transaction=("amount", "mean"),
    transaction_count=("amount", "count")
)

daily_summary = df.groupby("date").agg(
    daily_total=("amount", "sum"),
    transactions_per_day=("amount", "count")
)

plt.figure(figsize=(10, 6))
plt.bar(category_summary.index, category_summary["total_spent"])

plt.xlabel("Category")
plt.ylabel("Total Spending")
plt.title("Total Spending by Category")

plt.grid(alpha=0.5)

plt.savefig("plots/total_spending_by_category.png")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(daily_summary.index, daily_summary["daily_total"])

plt.xlabel("Date")
plt.ylabel("Total Spending")
plt.title("Daily Spending Over Time")

plt.grid(alpha=0.5)

plt.savefig("plots/daily_spending_over_time.png")
plt.show()
