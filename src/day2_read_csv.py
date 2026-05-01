import pandas as pd

# Read data
df = pd.read_csv("data/sample.csv")

print("Full Data:")
print(df)

# Filter data
filtered = df[df["age"] > 28]

print("\nFiltered Data (age > 28):")
print(filtered)

# Simple aggregation
avg_salary = df["salary"].mean()

print("\nAverage Salary:", avg_salary)