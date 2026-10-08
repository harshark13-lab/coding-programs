

import pandas as pd
import matplotlib.pyplot as plt

# Create student data
data = {
    "Name": ["Harsha", "Rahul", "Anita", "Priya", "Arjun"],
    "Marks": [85, 78, 92, 88, 75]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Student Data:")
print(df)

# Create a bar chart
plt.bar(df["Name"], df["Marks"])

# Add title and labels
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Display the chart
plt.show()
