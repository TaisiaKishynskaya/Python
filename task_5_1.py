from itertools import takewhile, count
from utils import get_name_string, get_intro_string

get_name_string()
get_intro_string()

if __name__ == '__main__':
    EPSILON = 0.0001  # accuracy
    row = (1 / pow(2, n) + 1 / pow(3, n) for n in count())  # series generator
    # the sum of the series with the specified accuracy:
    suma = sum(filter(lambda x: x != 0, takewhile(lambda x: x >= EPSILON, row)))

    print(f'The sum of the series with eps={EPSILON} accuracy is: {suma}')
