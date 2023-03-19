"""Introduction to programming’: Task 3,
   Kyshynska Taisiia"""
import math

print("""Introduction to programming’: Task 3
         Kyshynska Taisiia""")

x = float(input('x = '))
z = float(input('z = '))
y = (x + math.exp(z - 1)) / (1 - (x**2) * abs(x - z))

if (x**2) * abs(x - z) == 1:
    print('Значення змінних виходять за область визначення функції')
else:
    print(y)
