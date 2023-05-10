from itertools import takewhile, count
from utils import print_intro

EPSILON = 0.0001  # accuracy

print_intro()


def get_sum():
    # the sum of the series with the specified accuracy:
    row = (1 / pow(2, n) + 1 / pow(3, n) for n in count())  # series generator
    suma_row = round(sum(filter(lambda x: x != 0, takewhile(lambda x: x >= EPSILON, row))), 4)
    return suma_row


if __name__ == '__main__':
    suma = get_sum()
    print(f'The sum of the series with eps={EPSILON} accuracy is: {suma}')
