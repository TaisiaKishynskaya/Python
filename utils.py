def print_intro():
    print('Introduction to programming: Task 8-9')
    print('Kyshynska Taisiia')


def get_valid_number_input(variable):
    while True:
        try:
            return int(input(variable))
        except ValueError:
            print("Invalid input. Please input a number.")
