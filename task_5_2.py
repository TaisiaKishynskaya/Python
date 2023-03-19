"""Introduction to programming’: Task 2,
   Kyshynska Taisiia"""

print("""Introduction to programming’: Task 2
         Kyshynska Taisiia""")

n = int(input("Введіть ціле число: "))

k = 0  # лічильник цифр

while n != 0:
    n //= 10  # ділимо на 10, щоб відокремити останню цифру
    k += 1  # збільшуємо лічильник на 1

print("Кількість цифр у введеному числі: ", k)
