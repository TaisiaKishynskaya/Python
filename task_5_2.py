from utils import print_intro

print_intro()


def check_exit(exit_str):
    return exit_str == "exit"


if __name__ == '__main__':
    while True:
        n = input("Enter an integer: ")
        if check_exit(n):
            break

        # Checking for non-compliance
        while not n.isdigit():
            n = input("Please enter a positive integer without any symbols: ")
            if check_exit(n):
                break

        if check_exit(n):
            break

        count = len(n)

        print(f"The number of digits in the entered number: {count}")
