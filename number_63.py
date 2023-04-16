import numpy as np

a = np.array([1, 3, 7, 1, 2, 6, 0, 1])

peaks = []

for i in range(1, len(a)-1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        peaks.append(i)

print(peaks)
