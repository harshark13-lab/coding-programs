

import pandas as pd

# Create student data
data = {
    "Name": ["Harsha", "Rahul", "Anita", "Priya", "Arjun", "Kiran"],
    "Department": ["AIML", "CSE", "AIML", "CSE", "AIML", "CSE"],
    "Marks": [85, 78, 92, 88, 75, 82]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)

# Group students by department
grouped = df.groupby("Department")["Marks"].mean()

print("\nAverage marks by department:")
print(grouped)

# Find highest marks in each department
highest = df.groupby("Department")["Marks"].max()

print("\nHighest marks by department:")
print(highest)

# Count students in each department
count = df.groupby("Department")["Name"].count()

print("\nNumber of students in each department:")
print(count)
