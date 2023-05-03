from utils import print_intro

print_intro()

TEMPLATE = 'Input {} value: '


def get_input_value(input_variable):
    while True:
        try:
            return int(input(TEMPLATE.format(input_variable)))
        except ValueError as err:
            print(f'Error: {err}')
            print(f'Input a valid number for {input_variable}')


def validate_non_zero(input_variable):
    while True:
        input_val = get_input_value(input_variable)
        if input_val != 0:
            return input_val
        print(f'{input_variable} can not be zero.')


variables = {'x': get_input_value, 'y': validate_non_zero, 'z': get_input_value}

for input_value in variables:
    variables[input_value] = variables[input_value](input_value)


while True:
    print(((15 - variables['x']) / variables['y']) / (33 ** variables['y'] + 19.3) + variables['z'])
    change_input = input('Do you want to change x, y, z or exit? Input "x", "y", "z" or "exit": ').lower()
    if change_input == 'exit':
        break
    elif change_input in variables:
        variables[change_input] = get_input_value(change_input)
    else:
        print('Invalid input')


"""def get_input_value(input_variable):
    while True:
        try:
            return int(input(TEMPLATE.format(input_variable)))
        except ValueError as err:
            print(f'Error: {err}')
            print(f'Input a valid number for {input_variable}')


def validate_non_zero(input_variable):
    while True:
        input_value = get_input_value(input_variable)
        if input_value != 0:
            return input_value
        print(f'{input_variable} can not be zero.')


def apply_function(func, *args):
    return func(*args)


variables = {'x': get_input_value(input_variable='x'), 'y': validate_non_zero(input_variable='y'),
             'z': get_input_value(input_variable='z')}

while True:
    result = apply_function(
        lambda x=variables['x'], y=variables['y'], z=variables['z']: (15 - x / y) / (33 ** y + 19.3) + z())
    print(result)
    change_input = input('Do you want to change x, y, z or exit? Input "x", "y", "z" or "exit": ').lower()
    if change_input == 'exit':
        break
    elif change_input in variables:
        variables[change_input] = lambda input_variable=change_input: get_input_value(input_variable)
    else:
        print('Invalid input')"""