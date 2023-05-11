import sys


def validate_number(number_string):
    try:
        float(number_string)
        return True
    except ValueError:
        return False


def validate_input(input_lines):
    """Check that the list of input_lines is a valid list of numbers separated by a newline character"""
    # pylint: disable=unused-variable
    for i, the_line in enumerate(input_lines):
        if not isinstance(the_line, str):  # Check that the line is a string before converting to float
            return False
        if the_line.strip() == '':
            continue
        if not validate_number(the_line.strip()):
            return False
    return True


def validate_input_file(lines):
    if not validate_input(lines):
        print('Invalid input file. Numbers must start each time on a new line.')
        sys.exit()


def open_to_read():
    # open the file with numbers for reading
    try:
        with open('numbers.txt', 'r', encoding='utf-8') as numbers_file:
            # read all lines of the file and convert them into valid numbers
            lines = [line.strip() for line in numbers_file.readlines()]
            arr_numbers = [float(line) for line in lines if validate_number(line)]
            invalid_numbers = [line for line in lines if not validate_number(line)]
            for number in invalid_numbers:
                print(f'Invalid number: {number}')

            # validate the input file
            validate_input_file(lines)

    except FileNotFoundError:
        print("File 'numbers.txt' not found.")
        sys.exit()
    return arr_numbers


def open_to_write(summing_numbers):
    # open a file for writing the sum of numbers
    try:
        with open('sum_numbers.txt', 'w', encoding='utf-8') as sum_file:
            # write the sum of numbers to a file
            sum_file.write(str(summing_numbers))
    except IOError:
        print("An error occurred while writing to the file 'sum_numbers.txt'.")
        sys.exit()
    else:
        print("The sum has been written to the file 'sum_numbers.txt'")


if __name__ == '__main__':
    numbers = open_to_read()

    # calculate the sum of numbers
    sum_numbers = sum(numbers)

    # print the sum of numbers to the screen
    print(f'Sum of numbers: {sum_numbers}')

    open_to_write(sum_numbers)
