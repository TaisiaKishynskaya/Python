"""Introduction to programming’: Task 2,
   Kyshynska Taisiia"""

import math as m

print("""Introduction to programming’: Task 2
         Kyshynska Taisiia""")

eps = 1e-4  # accuracy
n = 1  # row member number
a = m.factorial(n) / (3 * n ** n)  # the first term of the series
suma = a  # initial amount

while abs(a) >= eps:
    n += 1
    a = m.factorial(n) / (3 * n ** n)
    suma += a

print("The sum of the series with eps=10^-4 accuracy is: ", suma)
