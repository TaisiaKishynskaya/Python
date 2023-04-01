import math as m
from utils import get_name_string, get_intro_string

print(get_intro_string())
print(get_name_string())


def get_input_value(variable):
    while True:
        value = input(f"{variable} = ")
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please input a number.")


def calculate_y(x_val, z_val):
    try:
        y_val = (x_val + m.exp(z_val - 1)) / (1 - (x_val ** 2) * abs(x_val - z_val))
        if (x_val ** 2) * abs(x_val - z_val) == 1:
            print('The values of the variables go beyond the scope of the function')
            return None
        else:
            return y_val
    except ZeroDivisionError:
        print('The denominator in the expression equals zero')
        return None


x = get_input_value('x')
z = get_input_value('z')

y = calculate_y(x, z)

while True:
    if y is not None:
        print(y)

    choice = input('Do you want to change the values of x or z? (y/n) ')
    if choice.lower() == 'y':
        var_choice = input('Which variable do you want to change? (x/z) ')

        if var_choice.lower() in ['x', 'z']:
            if var_choice.lower() == 'x':
                x = get_input_value('x')
            else:
                z = get_input_value('z')
        else:
            print('Invalid input')

        y = calculate_y(x, z)

        if y is not None:
            print(y)

    elif choice.lower() == 'n':
        break

    else:
        print('Invalid input')
