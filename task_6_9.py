def main():
    total_letters = len([char for char in text if char.isalpha()])  # calculate the total number of letters in the text
    lowercase_letters = len([char for char in text if char.islower()])  # calculate the number of lowercase letters

    percent_lowercase = lowercase_letters / total_letters * 100

    print(f'Percentage of lowercase letters: {percent_lowercase:.2f}%')
    print(f'Percentage of uppercase letters: {100 - percent_lowercase:.2f}%')


if __name__ == '__main__':
    with open('The Count of Monte Cristo.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    main()
