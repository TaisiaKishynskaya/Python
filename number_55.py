import numpy as np

np.random.seed(10)
a = np.random.randint(20, size=[2, 5])
print(a)

# Создаем массив индексов, расположенных в порядке возрастания
idx = np.argsort(a, axis=None)

# Создаем массив рангов, используя индексы
r = np.empty_like(idx)
r[idx] = np.arange(len(idx))

# Преобразуем массив рангов обратно в форму массива a
r = r.reshape(a.shape)

print(r)

