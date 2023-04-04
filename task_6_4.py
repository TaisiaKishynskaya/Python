FILE_NAME = 'learning_python.txt'

try:
    with open(FILE_NAME, encoding='utf-8') as file:
        lines = file.readlines()
except IOError:
    print(f'Ошибка: не удалось открыть файл {FILE_NAME} для чтения.')
else:
    print('Содержимое файла:')
    for line in lines:
        new_line = line.replace('Python', 'C')
        print(new_line.strip())
