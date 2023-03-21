import numpy as np

np.random.seed(100)
a = np.random.randint(0, 5, 10)
print('Array: ', a)

_, idx = np.unique(a, return_index=True)  # отримати індекси перших входжень кожного унікального елемента
repeats = np.ones_like(a, dtype=bool)  # створити логічний масив
repeats[idx] = False  # встановити значення на індексах перших входжень у False
repeats[0] = False  # встановити перший елемент у False, щоб перше входження було False

print('Repeating values: ', repeats)
