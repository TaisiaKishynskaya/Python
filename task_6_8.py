import re


def main():
    # Opening files for reading and writing
    with open('The Life and Adventures of Robinson Crusoe.txt', 'r', encoding='utf-8') as file, \
            open('chapters.txt', 'w', encoding='utf-8') as out_file:
        # Search for section headings using a regular expression
        chapter_titles = re.findall(r'CHAPTER [IVXLC]+—[A-Z\s’\-–—]+\.', file.read())
        # Write the found headers to a file
        for title in chapter_titles:
            out_file.write(title + '\n')


if __name__ == '__main__':
    main()
