from itertools import takewhile, count
from utils import print_intro

print_intro()


def get_sum(epsilon, my_row):
    # the sum of the series with the specified accuracy:
    suma_row = sum(filter(lambda x: x != 0, takewhile(lambda x: x >= epsilon, my_row)))
    print(f'The sum of the series with eps={epsilon} accuracy is: {suma_row}')
    return suma_row


if __name__ == '__main__':
    EPSILON = 0.0001  # accuracy
    row = (1 / pow(2, n) + 1 / pow(3, n) for n in count())  # series generator
    suma = get_sum(EPSILON, row)
