

student = ("Harsha", 21, "AIML", 85.5)

print("Student tuple:", student)

# Access elements
print("Name:", student[0])
print("Age:", student[1])
print("Course:", student[2])
print("Marks:", student[3])

# Find the length
print("Number of elements:", len(student))

# Check whether an element exists
if "AIML" in student:
    print("AIML is present in the tuple.")

# Count occurrences
print("Number of times 85.5 occurs:", student.count(85.5))

# Find the position of an element
print("Position of AIML:", student.index("AIML"))
