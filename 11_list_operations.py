
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# Add an element
numbers.append(60)
print("After adding 60:", numbers)

# Remove an element
numbers.remove(30)
print("After removing 30:", numbers)

# Access an element
print("First element:", numbers[0])

# Find the length
print("Number of elements:", len(numbers))

# Sort the list
numbers.sort()
print("Sorted list:", numbers)

# Find the maximum and minimum
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
