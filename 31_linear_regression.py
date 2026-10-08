
from sklearn.linear_model import LinearRegression
import numpy as np

# Training data
study_hours = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
marks = np.array([35, 40, 50, 55, 65, 70])

# Create the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(study_hours, marks)

# Predict marks for 7 hours of study
hours = np.array([[7]])
prediction = model.predict(hours)

print("Predicted marks for 7 hours of study:", prediction[0])

# Display the model's slope
print("Slope:", model.coef_[0])

# Display the model's intercept
print("Intercept:", model.intercept_)
