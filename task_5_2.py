import sys
from utils import print_intro

print_intro()


# Checking for non-compliance
def validate_isdigit(variable_n):
    while not variable_n.isdigit():
        variable_n = input("Please enter a positive integer without any symbols: ")
    return variable_n


def count_digits(var_n):
    var_count = 0
    num = int(var_n)
    # Counting digits
    while num > 0:
        num //= 10
        var_count += 1
    return var_count


def check_exit(exit_str):
    if exit_str == "exit":
        sys.exit(0)


if __name__ == '__main__':
    # pylint: disable=invalid-name
    while True:
        user_input = input('Enter "exit" if you like to finish the program: ')

        check_exit(user_input)
        user_input = validate_isdigit(user_input)
        count = count_digits(user_input)

        print(f'The number of digits in the entered number: {count}')
    # main()
