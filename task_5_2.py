"""Introduction to programming’: Task 2,
   Kyshynska Taisiia"""

print('Introduction to programming’: Task 2')
print('Kyshynska Taisiia')

while True:
    try:
        n = int(input('Enter an integer: '))
        break
    except ValueError:
        print("You didn't enter an integer. Please try again.")

k = 0  # digit counter

while n != 0:
    n //= 10  # divide by 10 to separate the last digit
    k += 1  # we increase the counter by 1

print(f'The number of digits in the entered number: {k}')
