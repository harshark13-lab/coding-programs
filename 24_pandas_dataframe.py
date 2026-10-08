

import pandas as pd

# Create data
data = {
    "Name": ["Harsha", "Rahul", "Anita", "Priya", "Arjun"],
    "Age": [21, 22, 20, 21, 23],
    "Marks": [85, 78, 92, 88, 75]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)

# Display first rows
print("\nFirst 3 students:")
print(df.head(3))

# Display column names
print("\nColumn names:")
print(df.columns)

# Display basic information
print("\nDataFrame information:")
print(df.info())

# Calculate average marks
print("\nAverage marks:", df["Marks"].mean())

# Find highest marks
print("Highest marks:", df["Marks"].max())
