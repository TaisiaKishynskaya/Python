import os


def validate_number(num_str):
    """Функция для проверки, является ли строка числом.
    Возвращает True, если строка является числом, и False в противном случае."""
    try:
        int(num_str)
        return True
    except ValueError:
        return False


def write_to_file(the_filename, the_text):
    """Функция для записи текста в файл с заданным именем."""
    with open(the_filename, 'w', encoding='utf-8') as file:
        file.write(the_text)


def check_even_odd(num):
    """Функция для определения четности числа и возврата текстовой строки."""
    if num == 0:
        result = 'neither even nor odd'
    elif num % 2 == 1:
        result = 'odd'
    else:
        result = 'even'
    return f'Число {num} - {result}.'


def get_integer_input():
    """Функция для получения от пользователя целого числа."""
    while True:
        input_str = input('Введите целое число: ')
        if not validate_number(input_str):
            print('Ошибка: введенное значение не является целым числом.')
            continue
        return int(input_str)


def write_result_to_file(text):
    """Функция для записи результата в файл."""
    filename = 'result.txt'
    if os.path.exists(filename):
        if not get_yes_no_input(f'Файл {filename} уже существует, перезаписать? (y/n): '):
            return False
    write_to_file(filename, text)
    print(f'Результат записан в файл {filename}.')


def ask_to_continue():
    """Функция для запроса у пользователя продолжения выполнения программы."""
    if get_yes_no_input(f'Хотите продолжить работу программы? (y/n): '):
        return True


def get_yes_no_input(prompt):
    """Функция для получения от пользователя ответа y/n на заданный вопрос."""
    while True:
        choice = input(prompt).lower()
        if choice == 'n':
            return False
        elif choice == 'y':
            return True
        else:
            print('Ошибка: неверный ввод. Введите "y" или "n".')
            continue


def main():
    while True:
        input_str = get_integer_input()

        # Преобразуем введенную строку в число
        num = int(input_str)

        text = check_even_odd(num)
        print(text)

        write_result_to_file(text)

        if not ask_to_continue():
            break


if __name__ == '__main__':
    main()
