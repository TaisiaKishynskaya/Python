from itertools import takewhile, count
from utils import get_name_string, get_intro_string

get_name_string()
get_intro_string()

EPSILON = 0.0001  # accuracy
row = (1 / pow(2, n) + 1 / pow(3, n) for n in count())  # series generator
# the sum of the series with the specified accuracy:
suma = 0
for term in takewhile(lambda x: x >= EPSILON, row):
    if term != 0:
        suma += term
    else:
        print('Error: denominator is zero')
        break

print(f'The sum of the series with eps={EPSILON} accuracy is: {suma}')
