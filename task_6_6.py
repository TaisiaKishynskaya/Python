import sys


if __name__ == '__main__':
    FILE_NAME = 'gutenberg.txt'

    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{FILE_NAME}' not found.")
        sys.exit()

    if not text:
        print('Error: File is empty.')
        sys.exit()

    # We divide the text into different texts using the new line symbol
    texts = text.split('\n')

    # We count the number of occurrences of the word "the" in each text
    for i, t in enumerate(texts):
        if not t:
            continue
        count = t.lower().count('the')
        print(f'Text {i + 1}: {count}')
