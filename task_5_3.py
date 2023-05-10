from utils import print_intro

print_intro()
EPSILON = 0.0001  # accuracy


def get_input():
    while True:
        try:
            a = float(input('Enter a positive number a: '))
            x1 = float(input('Enter any leading positive number x1: '))
            if a <= 0 or x1 <= 0:
                raise ValueError
            return a, x1
        except ValueError:
            print("Invalid input, please enter a positive number.")


def calculate_geron_sqrt(x1, a):
    xn = x1
    xn1 = 0.5 * (xn + a / xn)  # the first term of the sequence

    while abs(xn1 - xn) > EPSILON:  # until the required accuracy is achieved
        xn = xn1
        xn1 = 0.5 * (xn + a / xn)
    return round(xn1, 4)


if __name__ == '__main__':
    fist_val, second_val = get_input()
    xn1 = calculate_geron_sqrt(fist_val, second_val)
    print(f'The square root of a number {second_val} is {xn1}')
