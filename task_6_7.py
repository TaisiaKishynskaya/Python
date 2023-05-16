def main():
    with open('book.txt', 'r', encoding='utf-8') as file, \
            open('formatted_text.txt', 'w', encoding='utf-8') as out_file:
        text = file.read().replace('\n', ' ')
        out_file.write(text)


if __name__ == '__main__':
    main()
