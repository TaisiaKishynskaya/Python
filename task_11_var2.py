import re


def read_file():
    with open('text.txt', 'r', encoding='utf-8') as file:
        return file.read()


def main():
    sentences = re.split(r'[.?!]\s', read_file())
    print(sentences)


if __name__ == '__main__':
    main()
