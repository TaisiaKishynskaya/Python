import sys

FILE_NAME = 'gutenberg.txt'


def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit()
    return content


def count_occurrences(texts):
    for i, t in enumerate(texts):
        if not t:
            continue
        count = t.lower().count('the')
        print(f'Text {i + 1}: {count}')


if __name__ == '__main__':
    text = read_file(FILE_NAME)

    if not text:
        print('Error: File is empty.')
        sys.exit()

    # We divide the text into different texts using the new line symbol
    texts = text.split('\n')

    # We count the number of occurrences of the word "the" in each text
    count_occurrences(texts)
