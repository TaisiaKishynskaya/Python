"""Introduction to programming’: Task 2,
   Kyshynska Taisiia"""

print('Introduction to programming’: Task 2')
print('Kyshynska Taisiia')

TEMPLATE = "Input {} = "
while True:
    try:
        x = int(input(TEMPLATE.format('x')))
        y = int(input(TEMPLATE.format('y')))
        z = int(input(TEMPLATE.format('z')))
        break
    except ValueError:
        print("Error: Input numbers")

equal = ((15 - x / y) / (33 ** y + 19.3) + z)
print(equal)
