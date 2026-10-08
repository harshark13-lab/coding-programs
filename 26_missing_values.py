

import pandas as pd

# Create data with missing values
data = {
    "Name": ["Harsha", "Rahul", "Anita", "Priya", "Arjun"],
    "Age": [21, 22, None, 21, 23],
    "Marks": [85, None, 92, 88, 75]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Check for missing values
print("\nMissing values:")
print(df.isnull())

# Count missing values in each column
print("\nNumber of missing values:")
print(df.isnull().sum())

# Fill missing Age with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Marks with the average marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nData after filling missing values:")
print(df)
