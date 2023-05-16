import string


def count_letters(content, letter_type):
    """Counts the number of letters in the given text that match the specified letter type (lowercase or uppercase)"""
    letters = string.ascii_lowercase if letter_type == 'lowercase' else string.ascii_uppercase
    count = len([char for char in content if char.isalpha() and char in letters])
    return count


if __name__ == '__main__':
    with open('The Count of Monte Cristo.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    total_letters = len([char for char in text if char.isalpha()])  # calculate the total number of letters in the text
    lowercase_letters = count_letters(text, 'lowercase')  # calculate the number of lowercase letters
    uppercase_letters = count_letters(text, 'uppercase')  # calculate the number of uppercase letters

    percent_lowercase = lowercase_letters / total_letters * 100

    print(f'Percentage of lowercase letters: {percent_lowercase:.2f}%')
    print(f'Percentage of uppercase letters: {100 - percent_lowercase:.2f}%')
