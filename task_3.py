import math as m
from utils import print_intro, get_input_value
print_intro()


def calculate_y(x_val, z_val):
    if (x_val ** 2) * abs(x_val - z_val) == 1:
        print('The values of the variables go beyond the scope of the function')
    else:
        print((x_val + m.exp(z_val - 1)) / (1 - (x_val ** 2) * abs(x_val - z_val)))


x = get_input_value('x')
z = get_input_value('z')

while True:
    calculate_y(x, z)
    choice = input('Do you want to change the values of x or z? (y/n) ')
    if choice.lower() == 'y':
        var_choice = input('Which variable do you want to change? (x/z) ')

        if var_choice.lower() == 'x':
            x = get_input_value('x')
        elif var_choice.lower() == 'z':
            z = get_input_value('z')
        else:
            print('Invalid input')

    elif choice.lower() == 'n':
        break

    else:
        print('Invalid input')
