"""Introduction to programming’: Task 2,
   Kyshynska Taisiia"""

print('Introduction to programming’: Task 2')
print('Kyshynska Taisiia')

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

eps = 1e-4  # accuracy
xn = x1
xn1 = 0.5 * (xn + a / xn)  # the first term of the sequence

while abs(xn1 - xn) > eps:  # until the required accuracy is achieved
    xn = xn1
    xn1 = 0.5 * (xn + a / xn)

print(f'The square root of a number {a} is {xn1}')
