import json
import matplotlib.pyplot as plt
import pandas as pd

with open("data/api_data.json", "r") as f:
    api_data = json.load(f)

df = pd.DataFrame(api_data["transactions"])

df["date"] = pd.to_datetime(df["date"], errors="coerce")

df["category"] = df["category"].str.lower().str.strip().str.title().str.replace(r'\s+', ' ', regex=True)

total_cat_spending = (df.groupby("category")["amount"].sum().sort_values(ascending=True))

max_total_cat = total_cat_spending.idxmax()
total_colors = ["#64aded" if cat == max_total_cat else "#1F78C6" for cat in total_cat_spending.index]

plt.figure(figsize=(11, 6))

plt.barh(total_cat_spending.index, total_cat_spending.values, color=total_colors)

for value, cat in zip(total_cat_spending.values, total_cat_spending.index):
    plt.text(value + 2, cat, f"${value:.2f}", va="center")

plt.title("Total Spending per Category", fontweight="bold")
plt.xlabel("Spending")
plt.ylabel("Category")
plt.grid(alpha=0.5)

plt.savefig("category_total_spending.png")
plt.show()


summary_table = df.groupby("category").agg(
    total_spent=("amount", "sum"),
    avg_spent=("amount", "mean"),
    transaction_count=("amount", "count")
).sort_values(by="total_spent")

max_avg_cat = summary_table["avg_spent"].idxmax()
avg_colors = ["#9e72fc" if cat == max_avg_cat else "#7e42ff" for cat in summary_table["avg_spent"].index]

plt.figure(figsize=(11, 6))
plt.barh(summary_table["avg_spent"].index, summary_table["avg_spent"],
         color=avg_colors)

for value, cat in zip(summary_table["avg_spent"], summary_table["avg_spent"].index):
    plt.text(value + 2, cat, f"${value:.2f}", va="center")

plt.title("Average Spending per Category", fontweight="bold")
plt.xlabel("Spending")
plt.ylabel("Category")
plt.grid(alpha=0.5)

plt.savefig("category_avg_spending.png")
plt.show()

print(summary_table)
