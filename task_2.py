from utils import get_name_string, get_intro_string

print(get_intro_string())
print(get_name_string())

variables = ['x', 'y', 'z']
values = []
TEMPLATE = 'Input {} value: '


def get_input_value(input_variable):
    while True:
        try:
            input_value = int(input(TEMPLATE.format(input_variable)))
            if input_variable == 'y' and input_value == 0:
                raise ValueError('y cannot be zero')
            return input_value
        except ValueError as e:
            print(f'Error: {e}')
            print(f'Input a valid number for {input_variable}')


for var in variables:
    value = get_input_value(var)
    values.append(value)

x, y, z = values

while True:
    equal = ((15 - x / y) / (33 ** y + 19.3) + z)
    print(equal)
    change_input = input('Do you want to change x, y, z or exit? Input "x", "y", "z" or "exit": ').lower()
    if change_input == 'exit':
        break
    elif change_input in variables:
        index = variables.index(change_input)
        value = get_input_value(change_input)
        values[index] = value
        x, y, z = values
    else:
        print('Invalid input')
