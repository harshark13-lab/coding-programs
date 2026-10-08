

import pandas as pd

# Create student data
data = {
    "Name": ["Harsha", "Rahul", "Anita", "Priya", "Arjun"],
    "Age": [21, 22, 20, 21, 23],
    "Marks": [85, 78, 92, 88, 75]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Filter students with marks greater than 80
high_marks = df[df["Marks"] > 80]

print("\nStudents with marks greater than 80:")
print(high_marks)

# Filter students with age equal to 21
age_21 = df[df["Age"] == 21]

print("\nStudents who are 21 years old:")
print(age_21)
