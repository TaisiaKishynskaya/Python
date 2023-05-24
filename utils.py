def print_intro():
    print('Introduction to programming: Task 8-9')
    print('Kyshynska Taisiia')


def get_valid_number_input(variable, cast_func):
    while True:
        try:
            return cast_func(input(variable))
        except ValueError:
            print("Invalid input. Please input a number.")
