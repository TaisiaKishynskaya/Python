FILE_NAME = 'gutenberg.txt'


def read_file():
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        return file.read()


def count_occurrences(text):
    for i, item in enumerate(text):
        count = item.lower().count('the')
        print(f'Text {i + 1}: {count}')


if __name__ == '__main__':
    texts = read_file().split('\n')
    count_occurrences(texts)
