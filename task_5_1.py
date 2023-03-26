"""Introduction to programming’: Task 2,
   Kyshynska Taisiia"""

from itertools import takewhile, count

print('Introduction to programming’: Task 2')
print('Kyshynska Taisiia')

eps = 1e-4  # accuracy
row = (1 / pow(2, n) + 1 / pow(3, n) for n in count())  # series generator
suma = sum(list(takewhile(lambda x: x >= eps, row)))  # the sum of the series with the specified accuracy

print(f'The sum of the series with eps={eps} accuracy is: {suma}')
