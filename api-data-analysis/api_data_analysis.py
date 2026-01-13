import json
import matplotlib.pyplot as plt
import pandas as pd

with open("data/api_data.json", "r") as f:
    api_data = json.load(f)

df = pd.DataFrame(api_data["transactions"])

df["date"] = pd.to_datetime(df["date"], errors="coerce")

df["category"] = df["category"].str.lower().str.strip().str.title().str.replace(r'\s+', ' ', regex=True)

total_cat_spending = (df.groupby("category")["amount"].sum().sort_values(ascending=True))
avg_cat_spending = (df.groupby("category")["amount"].mean().sort_values(ascending=False))

max_cat = total_cat_spending.idxmax()
colors = ["#64aded" if cat == max_cat else "#1F78C6" for cat in total_cat_spending.index]

plt.figure(figsize=(11, 6))

plt.barh(total_cat_spending.index, total_cat_spending.values, color=colors)

for value, cat in zip(total_cat_spending.values, total_cat_spending.index):
    plt.text(value + 2, cat, f"${value:.2f}", va="center")

plt.title("Total Spending per Category", fontweight="bold")
plt.xlabel("Spending")
plt.ylabel("Category")
plt.grid(alpha=0.5)

plt.savefig("category_total_spending.png")
plt.show()
