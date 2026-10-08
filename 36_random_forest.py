

from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Training data
# [Study Hours, Attendance]
X = np.array([
    [1, 50],
    [2, 55],
    [3, 60],
    [4, 65],
    [5, 70],
    [6, 75],
    [7, 80],
    [8, 90]
])

# Target values
# 0 = Fail
# 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Create the Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X, y)

# New student's data
new_student = np.array([[6, 78]])

# Make prediction
prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")

# Display prediction probability
probability = model.predict_proba(new_student)

print("Probability of Fail:", probability[0][0])
print("Probability of Pass:", probability[0][1])
