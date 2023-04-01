def check_lucky_number(number):
    sum_first = 0
    sum_last = 0

    # We calculate the sum of the first and last three digits
    for i in range(3):
        sum_first += int(number[i])
        sum_last += int(number[i + 3])

    # We compare the sums of the first and last three digits
    if sum_first == sum_last:
        print("This is a lucky number!")
    else:
        print("This is not a lucky number.")


if __name__ == '__main__':

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
                check_lucky_number(my_str)
