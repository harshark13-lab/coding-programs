

student = {
    "name": "Harsha",
    "age": 21,
    "course": "AIML",
    "marks": 85
}

print("Student details:", student)

# Access values
print("Name:", student["name"])
print("Course:", student["course"])

# Add a new key-value pair
student["college"] = "New Horizon College of Engineering"
print("After adding college:", student)

# Update a value
student["marks"] = 90
print("Updated marks:", student["marks"])

# Remove a key-value pair
student.pop("age")
print("After removing age:", student)

# Display all keys
print("Keys:", student.keys())

# Display all values
print("Values:", student.values())
