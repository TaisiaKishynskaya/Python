import re
from utils import print_intro

print_intro()

FILE_NAME = 'dates.txt'


def normalize_dates(name_file):
    with open(name_file, 'r', encoding='utf-8') as file:
        data = file.read()

    # yyyy.mm.dd -> dd.mm.yyyy
    data = re.sub(r'(?<!\d)(\d{4})\.(\d{1,2})\.(\d{1,2})(?!\d)', r'\3.\2.\1', data)

    # yyyy/mm/dd -> dd.mm.yyyy
    data = re.sub(r'(?<!\d)(\d{4})/(\d{1,2})/(\d{1,2})(?!\d)', r'\3.\2.\1', data)

    # dd.mm.yyyy (day or month represented by a single digit) -> dd.mm.yyyy
    data = re.sub(r'(?<!\d)(\d{1,2})\.(\d{1,2})\.(\d{4})(?!\d)',
                  lambda m: f'{m.group(1):0>2}.{m.group(2):0>2}.{m.group(3)}', data)

    # dd/mm/yyyy (day or month represented by a single digit) -> dd.mm.yyyy
    data = re.sub(r'(?<!\d)(\d{1,2})/(\d{1,2})/(\d{4})(?!\d)',
                  lambda m: f'{m.group(1):0>2}.{m.group(2):0>2}.{m.group(3)}', data)

    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(data)


if __name__ == '__main__':
    normalize_dates(FILE_NAME)
