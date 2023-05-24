from utils import print_intro

print_intro()

EPSILON = 0.0001  # accuracy


def get_input():
    while True:
        try:
            var_a = float(input('Enter a positive number a: '))
            variable_x1 = float(input('Enter any leading positive number x1: '))
            if var_a <= 0 or variable_x1 <= 0:
                raise ValueError
            return var_a, variable_x1
        except ValueError:
            print("Invalid input, please enter a positive number.")


def calculate_geron_sqrt(var_x1, variable_a):
    var_xn = var_x1
    var_xn1 = 0.5 * (var_xn + variable_a / var_xn)  # the first term of the sequence

    while abs(var_xn1 - var_xn) > EPSILON:  # until the required accuracy is achieved
        var_xn = var_xn1
        var_xn1 = 0.5 * (var_xn + variable_a / var_xn)
    return round(var_xn1, 4)


if __name__ == '__main__':
    fist_val, second_val = get_input()
    xn1 = calculate_geron_sqrt(fist_val, second_val)
    print(f'The square root of a number {second_val} is {xn1}')
