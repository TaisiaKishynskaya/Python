def print_learning_python_file():
    with open('learning_python.txt', encoding='utf-8') as file:
        lines = file.readlines()
    if lines:
        print('File`s content:')
        for line in lines:
            print(line.strip())


if __name__ == '__main__':
    print_learning_python_file()
