
from sklearn.linear_model import LogisticRegression
import numpy as np

# Training data
# Study hours
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
])

# Target values
# 0 = Fail
# 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Create the Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X, y)

# Test with a new student
new_student = np.array([[6]])

# Make prediction
prediction = model.predict(new_student)

# Get probability
probability = model.predict_proba(new_student)

if prediction[0] == 1:
    print("Result: Pass")
else:
    print("Result: Fail")

print("Probability of Fail:", probability[0][0])
print("Probability of Pass:", probability[0][1])
