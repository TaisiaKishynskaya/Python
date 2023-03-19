"""Introduction to programming’: Task 2,
   Kyshynska Taisiia"""

print("""Introduction to programming’: Task 2
         Kyshynska Taisiia""")

a = float(input("Введіть додатнє число a: "))
x1 = float(input("Введіть будь-яке початкове додатне число x1: "))

eps = 1e-4  # точність
xn = x1
xn1 = 0.5 * (xn + a / xn)  # перший член послідовності

while abs(xn1 - xn) > eps:  # поки не досягнута необхідна точність
    xn = xn1
    xn1 = 0.5 * (xn + a / xn)

print("Квадратний корінь з числа", a, "дорівнює", xn1)
