import math as m
from utils import print_intro, get_input_value

print_intro()

MY_X = 'x'
MY_Z = 'z'


def calculate_y(x_val, z_val):
    if (x_val ** 2) * abs(x_val - z_val) == 1:
        print('The values of the variables go beyond the scope of the function')
    else:
        print((x_val + m.exp(z_val - 1)) / (1 - (x_val ** 2) * abs(x_val - z_val)))


x = get_input_value(MY_X)
z = get_input_value(MY_Z)

while True:
    calculate_y(x, z)
    choice = input('Do you want to change the values of x or z? (y/n) ')
    if choice.lower() == 'y':
        var_choice = input(f'Which variable do you want to change? ({MY_X}/{MY_Z}) ')

        if var_choice.lower() == MY_X:
            x = get_input_value(MY_X)
        elif var_choice.lower() == MY_Z:
            z = get_input_value(MY_Z)
        else:
            print('Invalid input')

    elif choice.lower() == 'n':
        break
    else:
        print('Invalid input')
