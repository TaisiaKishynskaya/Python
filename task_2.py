"""Introduction to programming’: Task 2,
   Kyshynska Taisiia"""

print('Introduction to programming’: Task 2')
print('Kyshynska Taisiia')

TEMPLATE = 'Input {} = '
while True:
    try:
        x = int(input(TEMPLATE.format('x')))
        y = int(input(TEMPLATE.format('y')))
        z = int(input(TEMPLATE.format('z')))
        break
    except ValueError:
        print('Error: Input numbers')

while True:
    equal = ((15 - x / y) / (33 ** y + 19.3) + z)
    print(equal)
    change_input = input('Do you want to change x, y, z or exit? Input "x", "y", "z" or "exit": ')
    if change_input.lower() == 'exit':
        break
    elif change_input.lower() == 'x':
        while True:
            try:
                x = int(input(TEMPLATE.format('x')))
                break
            except ValueError:
                print('Error: Input a number for x')
    elif change_input.lower() == 'y':
        while True:
            try:
                y = int(input(TEMPLATE.format('y')))
                break
            except ValueError:
                print('Error: Input a number for y')
    elif change_input.lower() == 'z':
        while True:
            try:
                z = int(input(TEMPLATE.format('z')))
                break
            except ValueError:
                print('Error: Input a number for z')
    else:
        print('Invalid input')
