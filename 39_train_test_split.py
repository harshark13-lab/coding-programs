

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Input data
# Study hours
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
])

# Target data
# Marks
y = np.array([35, 40, 48, 55, 60, 68, 72, 80, 85, 92])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Display the data
print("Training data:")
print(X_train)

print("\nTesting data:")
print(X_test)

print("\nTraining target values:")
print(y_train)

print("\nTesting target values:")
print(y_test)

# Create the model
model = LinearRegression()

# Train the model using training data
model.fit(X_train, y_train)

# Make predictions using test data
predictions = model.predict(X_test)

print("\nPredictions:")
print(predictions)
