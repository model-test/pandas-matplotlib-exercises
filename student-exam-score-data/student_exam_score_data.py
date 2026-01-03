import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("report.csv")

# First 5 rows
print(df.head(5))

major_scores = df.groupby("major")["exam_score"].mean()

figure, axes = plt.subplots(1, 2)

# Bar Chart
axes[0].bar(major_scores.index, major_scores.values,
        color="skyblue",
        edgecolor="black")

axes[0].set_title("Average Exam Score by Major", size=13)
axes[0].set_xlabel("Major", size=12)
axes[0].set_ylabel("Average Exam Score", size=12)

# Scatter Chart
axes[1].scatter(df["study_hours"], df["exam_score"],
                color="purple")

axes[1].set_title("Study Hours vs Exam Score", size=13)
axes[1].set_xlabel("Hours", size=12)
axes[1].set_ylabel("Score", size=12)

# Global Title
figure.suptitle("Student Exam Score Data", fontsize=16, fontweight="bold")

plt.tight_layout()
plt.savefig("sample_output.png")
plt.show()
