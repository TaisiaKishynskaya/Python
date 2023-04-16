import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])

distance = np.sqrt(np.sum((a - b) ** 2))
print(distance)
