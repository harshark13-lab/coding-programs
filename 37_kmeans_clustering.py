

from sklearn.cluster import KMeans
import numpy as np

# Customer data
# [Age, Spending Score]
X = np.array([
    [20, 20],
    [22, 25],
    [24, 22],
    [26, 30],
    [40, 70],
    [42, 75],
    [44, 72],
    [46, 80]
])

# Create the K-Means model
model = KMeans(n_clusters=2, random_state=42, n_init=10)

# Train the model
model.fit(X)

# Get cluster labels
labels = model.labels_

print("Cluster labels:")
print(labels)

# Display cluster centers
print("\nCluster centers:")
print(model.cluster_centers_)

# Predict the cluster for a new customer
new_customer = np.array([[25, 28]])

prediction = model.predict(new_customer)

print("\nNew customer's cluster:", prediction[0])
