import re
from utils import print_intro

print_intro()

file_name = 'dates.txt'


def normalize_dates(name_file):
    # Открываем файл с датами для чтения
    with open(name_file, 'r', encoding='utf-8') as file:
        data = file.read()

    # Заменяем даты в формате yyyy/mm/dd на dd.mm.yyyy
    data = re.sub(r'(?<!\d)(\d{4})/(\d{1,2})/(\d{1,2})(?!\d)', r'\3.\2.\1', data)

    # Заменяем даты в формате dd.mm.yyyy, где день или месяц могут быть представлены одной цифрой, на dd.mm.yyyy
    data = re.sub(r'(?<!\d)(\d{1,2})\.(\d{1,2})\.(\d{4})(?!\d)',
                  lambda m: f'{m.group(1):0>2}.{m.group(2):0>2}.{m.group(3)}', data)

    # Заменяем даты в формате dd/mm/yyyy, где день или месяц могут быть представлены одной цифрой, на dd.mm.yyyy
    data = re.sub(r'(?<!\d)(\d{1,2})/(\d{1,2})/(\d{4})(?!\d)',
                  lambda m: f'{m.group(1):0>2}.{m.group(2):0>2}.{m.group(3)}', data)

    # Записываем измененный текст в файл
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(data)


if __name__ == '__main__':
    normalize_dates(file_name)
