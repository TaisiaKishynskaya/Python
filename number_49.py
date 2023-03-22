import numpy as np

np.random.seed(100)
arr = np.random.randint(1, 11, size=(6, 10))

unique_counts = np.zeros(arr.shape[0])

for i in range(arr.shape[0]):
    unique, counts = np.unique(arr[i], return_counts=True)
    unique_counts[i] = len(unique)

print(unique_counts)
