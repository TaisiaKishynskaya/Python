from utils import print_intro

print_intro()


def validate_number_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def validate_operations(first_number, second_number, operation_func):
    try:
        return operation_func(first_number, second_number)
    except ZeroDivisionError:
        print("Division by zero!")
        return None


def calculate(num1, num2, oper):
    operations_result = None
    if oper == "+":
        operations_result = num1 + num2
    elif oper == "-":
        operations_result = num1 - num2
    elif oper == "*":
        operations_result = num1 * num2
    elif oper == "/":
        operations_result = validate_operations(num1, num2, lambda x, y: x / y)
    elif oper == "mod":
        operations_result = validate_operations(num1, num2, lambda x, y: x % y)
    elif oper == "pow":
        operations_result = num1 ** num2
    elif oper == "div":
        operations_result = validate_operations(num1, num2, lambda x, y: x // y)
    else:
        print("Invalid operation")
    return operations_result


if __name__ == '__main__':
    first_num = validate_number_input("Enter the first number: ")
    second_num = validate_number_input("Enter the second number: ")
    operation = input("Enter the operation (+, -, /, *, mod, pow, div): ")

    result = calculate(first_num, second_num, operation)

    if result is not None:
        print(result)
