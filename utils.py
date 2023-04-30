def print_intro():
    print('Introduction to programming: Task 3')
    print('Kyshynska Taisiia')


def get_input_value(variable):
    while True:
        value = input(f"{variable} = ")
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please input a number.")
