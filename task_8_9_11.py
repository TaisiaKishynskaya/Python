from utils import print_intro, validate_number_input

print_intro()


def get_valid_number_input(message):
    number = input(message)
    while not validate_number_input(number):
        number = input(message)
    return int(number)


def convert_decimal_to_binary():
    decimal_num = get_valid_number_input('Enter a decimal number: ')

    binary_num = ''
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2

    print(f'{decimal_num} in Decimal is {binary_num} in Binary')


def convert_binary_to_decimal():
    binary_num = input('Enter a binary number: ')
    while not all(char in '01' for char in binary_num):
        binary_num = input('Invalid input. Please enter a valid binary number: ')

    decimal_num = 0
    power = 0

    for digit in binary_num[::-1]:
        decimal_num += int(digit) * 2 ** power
        power += 1

    print(f'{binary_num} in Binary is {decimal_num} in Decimal')


if __name__ == '__main__':
    convert_decimal_to_binary()
    convert_binary_to_decimal()
