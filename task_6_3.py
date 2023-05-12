FILENAME = 'learning_python.txt'


def write_to_file(file_name, my_lines):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:  # Здесь код для записи в файл
            file.writelines(my_lines)
    except IOError:
        print(f'Error: could not open file {file_name} for writing.')


def read_file(the_filename):
    try:
        with open(the_filename, encoding='utf-8') as file:
            the_lines = file.readlines()
    except IOError:
        print(f'Error: could not open file {the_filename} for reading.')
        return None
    return the_lines


def create_learning_python_file(filename):
    lines = ['In Python you can easily manipulate strings.\n',
             'In Python you can use a variety of data structures.\n',
             'In Python you can write modular and reusable code.\n']
    write_to_file(filename, lines)
    return filename


def print_learning_python_file():
    lines = read_file(FILENAME)
    if lines:
        print('File`s content:')
        for line in lines:
            print(line.strip())


if __name__ == '__main__':
    create_learning_python_file(FILENAME)
    print_learning_python_file()
