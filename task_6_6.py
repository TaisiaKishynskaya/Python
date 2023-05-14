FILE_NAME = 'gutenberg.txt'


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def count_occurrences(text):
    for i, text in enumerate(text):
        count = text.lower().count('the')
        print(f'Text {i + 1}: {count}')


if __name__ == '__main__':
    texts = read_file(FILE_NAME).split('\n')
    count_occurrences(texts)
