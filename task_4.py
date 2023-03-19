"""Introduction to programming’: Task 4,
   Kyshynska Taisiia"""

print("""Introduction to programming’: Task 4
         Kyshynska Taisiia""")

my_str = input('Input six-digit number: ')
sum_first = 0
sum_last = 0

# Перевіряємо, чи введено шестизначне число
if len(my_str) == 6:
    # Обчислюємо суму перших та останніх трьох цифр
    for i in range(3):
        sum_first += int(my_str[i])
        sum_last += int(my_str[i + 3])

    # Порівнюємо суми перших та останніх трьох цифр
    if sum_first == sum_last:
        print("This is a lucky number!")
    else:
        print("This is not a lucky number.")
else:
    print("Input six-digit number!")
