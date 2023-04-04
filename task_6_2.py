import os


def is_valid_number(num_str):
    """Функция для проверки, является ли строка числом.
    Возвращает True, если строка является числом, и False в противном случае."""
    try:
        int(num_str)
        return True
    except ValueError:
        return False


def is_odd(the_num):
    """Функция для проверки, является ли число нечетным.
    Возвращает True, если число нечетное, и False в противном случае."""
    return the_num % 2 == 1


def write_to_file(the_filename, the_text):
    """Функция для записи текста в файл с заданным именем."""
    with open(the_filename, 'w', encoding='utf-8') as file:
        file.write(the_text)


def main():
    while True:
        # Получаем число от пользователя и проверяем его
        input_str = input('Введите целое число: ')
        if not is_valid_number(input_str):
            print('Ошибка: введенное значение не является целым числом.')
            continue

        # Преобразуем введенную строку в число
        num = int(input_str)

        # Определяем, является ли число нечетным, и выводим соответствующее сообщение на экран
        result = 'нечетное' if is_odd(num) else 'четное'
        print(f'Число {num} - {result}.')
        text = f'Число {num} - {result}.'

        # Создаем файл и записываем в него текст
        filename = 'result.txt'
        if os.path.exists(filename):
            choice = input(f'Файл {filename} уже существует, перезаписать? (y/n): ')
            if choice.lower() == 'n':
                break
        write_to_file(filename, text)
        print(f'Результат записан в файл {filename}.')

        # Проверяем, хочет ли пользователь продолжить выполнение программы
        choice = input('Хотите продолжить выполнение программы? (y/n): ')
        if choice.lower() == 'n':
            break


if __name__ == '__main__':
    main()
