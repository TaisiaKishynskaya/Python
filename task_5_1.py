"""Introduction to programming’: Task 2,
   Kyshynska Taisiia"""

print("""Introduction to programming’: Task 2
         Kyshynska Taisiia""")

import math

eps = 1e-4  # точність
n = 1  # номер члена ряду
a = math.factorial(n) / (3 * n**n)  # перший член ряду
sum = a  # початкова сума

while abs(a) >= eps:
    n += 1
    a = math.factorial(n) / (3 * n**n)
    sum += a

print("Сума ряду з точністю eps=10^-4 дорівнює:", sum)

