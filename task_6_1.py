def validate_number(number_string):
    try:
        float(number_string)
        return True
    except ValueError:
        return False


def validate_input(input_line):
    """Check that the input_line is a valid number"""
    if not input_line.strip():
        return True  # Skip empty lines
    return validate_number(input_line.strip())


def open_to_read():
    # open the file with numbers for reading
    try:
        with open('numbers.txt', 'r', encoding='utf-8') as numbers_file:
            # read the file line by line and filter out invalid numbers
            return [float(line) for line in numbers_file if validate_input(line)]
    except FileNotFoundError:
        print("File 'numbers.txt' not found.")
        return []


def open_to_write(summing_numbers):
    # open a file for writing the sum of numbers
    try:
        with open('sum_numbers.txt', 'w', encoding='utf-8') as sum_file:
            # write the sum of numbers to a file
            sum_file.write(str(summing_numbers))
    except IOError:
        print("An error occurred while writing to the file 'sum_numbers.txt'.")
    else:
        print("The sum has been written to the file 'sum_numbers.txt'")


if __name__ == '__main__':
    sum_numbers = sum(open_to_read())  # # calculate the sum of numbers
    print(f'Sum of numbers: {sum_numbers}')
    open_to_write(sum_numbers)
