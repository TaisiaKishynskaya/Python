def check_even_odd(num):
    """Функция для определения четности числа и возврата текстовой строки."""
    if num == 0:
        result = 'neither even nor odd'
    elif num % 2 == 1:
        result = 'odd'
    else:
        result = 'even'
    return f'Число {num} - {result}.'


def write_result_to_file(text):
    """Функция для записи результата в файл."""
    filename = 'result.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(check_even_odd(text))
    print(f'Результат записан в файл {filename}.')


if __name__ == '__main__':
    number = int(input('Введите целое число: '))
    write_result_to_file(number)
