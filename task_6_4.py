def open_file(file_name):
    try:
        with open(file_name, encoding='utf-8') as it_file:
            return it_file
    except IOError:
        print(f'Error: could not open file {file_name} for reading.')
        return None


def read_file(the_file):
    if the_file is None:
        return []
    the_lines = the_file.readlines()
    return the_lines


def replace_and_print(our_lines):
    if our_lines is None:
        return []
    print('File contents:')
    for line in our_lines:
        new_line = line.replace('Python', 'C')
        print(new_line.strip())
    return our_lines


if __name__ == '__main__':
    FILE_NAME = 'learning_python.txt'
    file = open_file(FILE_NAME)
    lines = read_file(file)
    replace_and_print(lines)
