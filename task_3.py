"""Introduction to programming’: Task 3,
   Kyshynska Taisiia"""
import math as m

print('Introduction to programming’: Task 2')
print('Kyshynska Taisiia')

TEMPLATE = '{} = '
x = float(input(TEMPLATE.format('x')))
z = float(input(TEMPLATE.format('z')))

if isinstance(x, (int, float)) and isinstance(z, (int, float)): # для проверки того, что переменные x и z являются числами,
    y = (x + m.exp(z - 1)) / (1 - (x ** 2) * abs(x - z)) #а затем продолжаем выполнение кода, если это так.

    if (x**2) * abs(x - z) == 1:
        print('The values of the variables go beyond the scope of the function')
    else:
        print(y)
else:
    print('You need to input nambers')

