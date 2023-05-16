def print_intro():
    print('Introduction to programming: Task 8-9')
    print('Kyshynska Taisiia')


def validate_number_input(input_str):
    try:
        int(input_str)
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        return False
    return True
