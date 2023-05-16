FILENAME = 'result.txt'


def check_even_odd(num):
    result = 'neither even nor odd'
    if num != 0:
        result = 'odd' if num % 2 == 1 else 'even'
    return f'Число {num} - {result}.'


def write_result_to_file(text):
    with open(FILENAME, 'w', encoding='utf-8') as file:
        file.write(check_even_odd(text))
    print(f'The result is written to a file {FILENAME}.')


if __name__ == '__main__':
    number = int(input('Enter integer number: '))
    write_result_to_file(number)
