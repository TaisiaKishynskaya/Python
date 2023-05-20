def replace_and_print():
    with open('learning_python.txt', encoding='utf-8') as file:
        return print('\n'.join([line.strip().replace('Python', 'C') for line in file]))


if __name__ == '__main__':
    replace_and_print()
