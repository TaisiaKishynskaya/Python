if __name__ == '__main__':
    filename = "gutenberg.txt"

    try:
        with open(filename, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit()

    if not text:
        print("Error: File is empty.")
        exit()

    # Розділяємо текст на різні тексти за допомогою символу нового рядка
    texts = text.split('\n')

    # Підраховуємо кількість входжень слова "the" в кожному тексті
    for i, t in enumerate(texts):
        if not t:
            continue
        count = t.lower().count("the")
        print(f"Text {i + 1}: {count}")
