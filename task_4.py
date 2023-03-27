print('Introduction to programming: Task 2')
print('Kyshynska Taisiia')

while True:
    my_str = input('Input six-digit number or type "exit" to quit: ')

    # we check that the user does not want to log out
    if my_str.lower() == "exit":
        break

    # we check that the number is entered
    if not my_str.isdigit():
        print("Input a number!")
    else:
        # we check that the number is six-digit
        if len(my_str) != 6:
            print("Input a six-digit number!")
        else:
            SUM_FIRST = 0
            SUM_LAST = 0

            # We calculate the sum of the first and last three digits
            for i in range(3):
                SUM_FIRST += int(my_str[i])
                SUM_LAST += int(my_str[i + 3])

            # We compare the sums of the first and last three digits
            if SUM_FIRST == SUM_LAST:
                print("This is a lucky number!")
            else:
                print("This is not a lucky number.")
