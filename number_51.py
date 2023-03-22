import numpy as np
from sklearn.preprocessing import OneHotEncoder

np.random.seed(101)
arr = np.random.randint(1, 4, size=6)

# Преобразуем массив в столбец и применяем OneHotEncoder
arr_2d = arr.reshape(-1, 1)
encoder = OneHotEncoder(categories='auto')
one_hot_encoded = encoder.fit_transform(arr_2d).toarray()

print("Source array:\n", arr)
print("\nOne-time encodings:\n", one_hot_encoded)
