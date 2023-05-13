with open('book.txt', 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', ' ')

with open('formatted_text.txt', 'w', encoding='utf-8') as file:
    file.write(text)
