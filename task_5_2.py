from utils import print_intro

print_intro()


# Checking for non-compliance
def validate_isdigit(n):
    while not n.isdigit():
        n = input("Please enter a positive integer without any symbols: ")
    return n


def count_digits(n):
    count = 0
    num = int(n)
    # Counting digits
    while num > 0:
        num //= 10
        count += 1
    return count


def check_exit(exit_str):
    if exit_str == "exit":
        exit(0)


if __name__ == '__main__':
    while True:
        n = input('Enter "exit" if you like to finish the program: ')

        check_exit(n)
        n = validate_isdigit(n)
        count = count_digits(n)

        print(f'The number of digits in the entered number: {count}')
