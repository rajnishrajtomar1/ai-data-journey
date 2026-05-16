import pandas as pd

# Load data
df = pd.read_csv("data/sample.csv")

# Add derived column (salary category)
def salary_band(salary):
    if salary < 55000:
        return "Low"
    elif salary < 65000:
        return "Medium"
    else:
        return "High"

df["salary_band"] = df["salary"].apply(salary_band)

# Filter dataset
filtered = df[df["age"] > 28]

# Aggregation
grouped = df.groupby("salary_band")["salary"].mean().reset_index()

print("Transformed Data:")
print(df)

print("\nFiltered Data (age > 28):")
print(filtered)

print("\nAverage Salary by Band:")
print(grouped)