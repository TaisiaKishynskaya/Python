import re
from utils import print_intro

print_intro()

FILE_NAME = 'dates.txt'
YYYY_XX_DD_TEMPLATE = r'(?<!\d)(\d{4})[./](\d{1,2})[./](\d{1,2})(?!\d)'
DD_XX_YYYY_TEMPLATE = r'(?<!\d)(\d{1,2})[./](\d{1,2})[./](\d{4})(?!\d)'
DATE_REPLACEMENT_TEMPLATE = r'\3.\2.\1'


def normalize_dates(name_file):
    with open(name_file, 'r', encoding='utf-8') as file:
        data = file.read()

    # yyyy.mm.dd (yyyy/mm/dd) -> dd.mm.yyyy
    data = re.sub(YYYY_XX_DD_TEMPLATE, DATE_REPLACEMENT_TEMPLATE, data)

    # dd.mm.yyyy(dd/mm/yyyy) (day or month represented by a single digit) -> dd.mm.yyyy
    data = re.sub(DD_XX_YYYY_TEMPLATE,
                  lambda m: f'{m.group(1):0>2}.{m.group(2):0>2}.{m.group(3)}', data)

    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(data)


if __name__ == '__main__':
    normalize_dates(FILE_NAME)
