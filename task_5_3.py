from utils import print_intro

print_intro()

while True:
    try:
        a = float(input('Enter a positive number a: '))
        if a <= 0:
            raise ValueError
        x1 = float(input('Enter any leading positive number x1: '))
        if x1 <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input, please enter a positive number.")

EPSILON = 0.0001  # accuracy
xn = x1
xn1 = 0.5 * (xn + a / xn)  # the first term of the sequence

while abs(xn1 - xn) > EPSILON:  # until the required accuracy is achieved
    xn = xn1
    xn1 = 0.5 * (xn + a / xn)

print(f'The square root of a number {a} is {xn1}')
