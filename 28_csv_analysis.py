

import pandas as pd

# Create a sample CSV file
data = {
    "Name": ["Harsha", "Rahul", "Anita", "Priya", "Arjun"],
    "Age": [21, 22, 20, 21, 23],
    "Marks": [85, 78, 92, 88, 75]
}

df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv("students.csv", index=False)

print("CSV file created successfully.")

# Read the CSV file
students = pd.read_csv("students.csv")

print("\nStudent Data:")
print(students)

# Display basic information
print("\nNumber of students:", len(students))

print("Average marks:", students["Marks"].mean())

print("Highest marks:", students["Marks"].max())

print("Lowest marks:", students["Marks"].min())

# Find the student with the highest marks
top_student = students.loc[students["Marks"].idxmax()]

print("\nStudent with highest marks:")
print(top_student)
