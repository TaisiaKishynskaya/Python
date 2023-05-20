def read_file():
    with open('gutenberg.txt', 'r', encoding='utf-8') as file:
        return file.readlines()


def count_occurrences():
    for i, line in enumerate(read_file()):
        count = line.lower().count('the')
        print(f'Text {i + 1}: {count}')


if __name__ == '__main__':
    count_occurrences()
