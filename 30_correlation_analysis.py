

import pandas as pd

# Create student data
data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8],
    "Attendance": [60, 65, 70, 75, 80, 85, 90],
    "Marks": [55, 60, 65, 72, 78, 85, 92]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)

# Calculate correlation matrix
correlation = df.corr()

print("\nCorrelation Matrix:")
print(correlation)

# Find correlation between study hours and marks
study_marks = df["Study_Hours"].corr(df["Marks"])

print("\nCorrelation between Study Hours and Marks:")
print(study_marks)

# Find correlation between attendance and marks
attendance_marks = df["Attendance"].corr(df["Marks"])

print("\nCorrelation between Attendance and Marks:")
print(attendance_marks)
