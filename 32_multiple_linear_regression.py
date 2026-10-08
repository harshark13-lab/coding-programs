

from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
# Columns: Study Hours, Attendance
X = np.array([
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85]
])

# Target values
marks = np.array([45, 50, 58, 65, 72, 80])

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, marks)

# New student's data
# Study Hours = 8
# Attendance = 90
new_student = np.array([[8, 90]])

# Make prediction
prediction = model.predict(new_student)

print("Predicted marks:", prediction[0])

# Display model coefficients
print("Coefficients:", model.coef_)

# Display intercept
print("Intercept:", model.intercept_)
