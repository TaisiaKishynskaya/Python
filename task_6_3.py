def write_to_file(my_filename, my_lines):
    try:
        with open(my_filename, 'w', encoding='utf-8') as file:  # Здесь код для записи в файл
            file.writelines(my_lines)
    except IOError:
        print(f'Ошибка: не удалось открыть файл {my_filename} для записи.')


def read_file(the_filename):
    try:
        with open(the_filename, encoding='utf-8') as file:
            the_lines = file.readlines()
    except IOError:
        print(f'Ошибка: не удалось открыть файл {the_filename} для чтения.')
        return None

    return the_lines


if __name__ == '__main__':
    FILENAME = 'learning_python.txt'

    lines = ['In Python you can easily manipulate strings.\n',
             'In Python you can use a variety of data structures.\n',
             'In Python you can write modular and reusable code.\n']
    write_to_file(FILENAME, lines)

    lines = read_file(FILENAME)
    if lines:
        print('Содержимое файла:')
        for line in lines:
            print(line.strip())
