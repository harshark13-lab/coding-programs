

import numpy as np

matrix_a = np.array([
    [1, 2],
    [3, 4]
])

matrix_b = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(matrix_a)

print("\nMatrix B:")
print(matrix_b)

# Addition
print("\nMatrix Addition:")
print(matrix_a + matrix_b)

# Subtraction
print("\nMatrix Subtraction:")
print(matrix_a - matrix_b)

# Element-wise multiplication
print("\nElement-wise Multiplication:")
print(matrix_a * matrix_b)

# Matrix multiplication
print("\nMatrix Multiplication:")
print(matrix_a @ matrix_b)

# Transpose
print("\nTranspose of Matrix A:")
print(matrix_a.T)
