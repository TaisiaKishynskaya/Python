import numpy as np

arr = np.arange(15)
window_size = 4
stride = 2

# обчислюємо розміри матриці та її форму
num_windows = ((arr.size - window_size) // stride) + 1
shape = (num_windows, window_size)
strides = (arr.itemsize * stride, arr.itemsize)

# створюємо матрицю, використовуючи stride tricks
matrix = np.lib.stride_tricks.as_strided(arr, shape=shape, strides=strides)

print(matrix)
