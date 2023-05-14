def replace_and_print():
    with open('learning_python.txt', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        new_line = line.replace('Python', 'C')
        print(new_line.strip())


if __name__ == '__main__':
    replace_and_print()
