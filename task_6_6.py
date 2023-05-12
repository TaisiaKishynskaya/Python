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


def read_and_split_file(file_name):
    try:
        return read_file(file_name).split('\n')
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit()


def count_occurrences(arr_texts):
    for i, text in enumerate(arr_texts):
        if not text:
            continue
        count = text.lower().count('the')
        print(f'Text {i + 1}: {count}')


if __name__ == '__main__':
    texts = read_and_split_file(FILE_NAME)
    count_occurrences(texts)  # We count the number of occurrences of the word "the" in each text
