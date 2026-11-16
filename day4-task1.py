import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

print(df.head())

avg_salary = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
bars = plt.bar(avg_salary.index, avg_salary.values)


plt.title("Averasge Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():0f}",
        ha="center",
        va="bottom"
    )

plt.savefig("bar_chart.png")
plt.show()


plt.figure(figsize=(8, 5))
plt.hist(df["salary"], bins=5, edgecolor="black")

plt.title("salary Distribution")
plt.xlabel("salary")
plt.ylabel("number of employees")

plt.savefig("histogram.png")
plt.show()

plt.figure(figsize=(8, 5))

for department in df["department"].unique():
    data = df[df["department"] == department]
    plt.scatter(
        data["id"],
        data["salary"],
        label=department
    )

plt.title("employee ID vs Salary")
plt.xlabel("employee ID")
plt.ylabel("salary")
plt.legend()

plt.savefig("scatter_plot.png")
plt.show()

months = ["jan", "feb", "mar", "apr", "may", "jun"]
sales =[12,15, 14, 18, 22, 25]
plt.figure(figsize=(8, 5))
plt.plot(months, sales, marker="o", label="monthly sales")

plt.title("monthly sales")
plt.xlabel("months")
plt.ylabel("sales")

plt.legend()

plt.savefig("line_chart.png")
plt.show()


plt.savefig("bar_chart.png")
plt.savefig("histogram.png")
plt.savefig("scatter_plot.png")
plt.savefig("line_chart.png")
