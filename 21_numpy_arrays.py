
import numpy as np

# Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50])

print("NumPy array:", numbers)

# Display the type
print("Type:", type(numbers))

# Display the shape
print("Shape:", numbers.shape)

# Display the size
print("Number of elements:", numbers.size)

# Mathematical operations
print("Array + 10:", numbers + 10)
print("Array * 2:", numbers * 2)

# Find statistics
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))
