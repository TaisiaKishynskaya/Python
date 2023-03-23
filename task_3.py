"""Introduction to programming’: Task 3,
   Kyshynska Taisiia"""

import math as m

print('Introduction to programming’: Task 2')
print('Kyshynska Taisiia')

TEMPLATE = '{} = '

while True:
    x_input = input(TEMPLATE.format('x'))
    try:
        x = float(x_input)
        break
    except ValueError:
        print('Invalid input. Please input a number.')

while True:
    z_input = input(TEMPLATE.format('z'))
    try:
        z = float(z_input)
        break
    except ValueError:
        print('Invalid input. Please input a number.')

while True:
    y = (x + m.exp(z - 1)) / (1 - (x ** 2) * abs(x - z))
    if (x ** 2) * abs(x - z) == 1:
        print('The values of the variables go beyond the scope of the function')
        break
    else:
        print(y)
        break

while True:
    choice = input('Do you want to change the values of x or z? (y/n) ')
    if choice.lower() == 'y':
        var_choice = input('Which variable do you want to change? (x/z) ')

        while True:
            new_value = input('Enter the new value: ')

            try:
                new_value = float(new_value)
                break
            except ValueError:
                print('Invalid input. Please input a number.')

        if var_choice.lower() == 'x':
            x = new_value
        elif var_choice.lower() == 'z':
            z = new_value
        else:
            print('Invalid input')

        while True:
            y = (x + m.exp(z - 1)) / (1 - (x ** 2) * abs(x - z))

            if (x ** 2) * abs(x - z) == 1:
                print('The values of the variables go beyond the scope of the function')
                break
            else:
                print(y)
                break

    elif choice.lower() == 'n':
        break

    else:
        print('Invalid input')
        print(y)
