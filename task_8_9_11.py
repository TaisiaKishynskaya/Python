from utils import print_intro

print_intro()


def convert_decimal_to_binary():
    decimal_num = int(input("Enter a decimal number: "))
    binary_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num = decimal_num // 2
    print(f"{decimal_num} in Decimal is {binary_num} in Binary")


def convert_binary_to_decimal():
    binary_num = input("Enter a binary number: ")
    decimal_num = 0
    power = 0  # to keep track of the current power of two

    # to loop through the digits in reverse order, coz we start with the values of the smaller digits
    for digit in binary_num[::-1]:
        decimal_num += int(digit) * 2 ** power
        power += 1  # increases with each new digit in the binary number

    print(f"{binary_num} in Binary is {decimal_num} in Decimal")


if __name__ == '__main__':
    convert_decimal_to_binary()
    convert_binary_to_decimal()
