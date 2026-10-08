

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Training data
# [Study Hours, Attendance]
X = np.array([
    [1, 50],
    [2, 55],
    [2, 60],
    [3, 65],
    [6, 80],
    [7, 85],
    [8, 90],
    [9, 95]
])

# Target values
# 0 = Fail
# 1 = Pass
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# Create the KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X, y)

# New student's data
new_student = np.array([[7, 82]])

# Make prediction
prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")
