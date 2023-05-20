def read_learning_python_file():
    with open('learning_python.txt', encoding='utf-8') as file:
        lines = file.readlines()
    print('File\'s content:')
    if lines:
        return print('\n'.join(line.strip() for line in lines))
    return ''


if __name__ == '__main__':
    read_learning_python_file()
