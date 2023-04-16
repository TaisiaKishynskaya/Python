import numpy as np

arr = np.arange(9).reshape(3, 3)
reversed_arr = arr[:, ::-1]

print(reversed_arr)
