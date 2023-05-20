from utils import print_intro

print_intro()


def validate_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Invalid input. Please enter a valid number.')


def validate_operations(first_number, second_number, operation_func):
    try:
        return operation_func(first_number, second_number)
    except ZeroDivisionError:
        print('Division by zero!')
        return None


def calculate(num1, num2, oper):
    # pylint: disable=too-many-return-statements
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2
    if oper == '/':
        return validate_operations(num1, num2, lambda x, y: x / y)
    if oper == 'mod':
        return validate_operations(num1, num2, lambda x, y: x % y)
    if oper == 'pow':
        return num1 ** num2
    if oper == 'div':
        return validate_operations(num1, num2, lambda x, y: x // y)
    return None


if __name__ == '__main__':
    first_num = validate_number_input('Enter the first number: ')
    second_num = validate_number_input('Enter the second number: ')
    operation = input('Enter the operation (+, -, /, *, mod, pow, div): ')

    result = calculate(first_num, second_num, operation)

    if result:
        print(result)
