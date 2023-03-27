"""Introduction to programming’: Task 2,
   Kyshynska Taisiia"""

from itertools import takewhile, count

print('Introduction to programming’: Task 2')
print('Kyshynska Taisiia')

EPSILON = 0.0001  # accuracy
row = (1 / pow(2, n) + 1 / pow(3, n) for n in count())  # series generator
# the sum of the series with the specified accuracy:
suma = sum(list(takewhile(lambda x: x >= EPSILON, row)))

print(f'The sum of the series with eps={EPSILON} accuracy is: {suma}')
