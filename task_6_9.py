import string


def count_letters(content, letter_type):
    """Counts the number of letters in the given text that match the specified letter type (lowercase or uppercase)"""
    if letter_type == 'lowercase':
        letters = string.ascii_lowercase
    elif letter_type == 'uppercase':
        letters = string.ascii_uppercase
    else:
        raise ValueError('Invalid letter type')
    count = len([char for char in content if char.isalpha() and char in letters])
    return count


if __name__ == '__main__':
    with open('The Count of Monte Cristo.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    total_letters = len([char for char in text if char.isalpha()])  # calculate the total number of letters in the text
    lowercase_letters = count_letters(text, 'lowercase')  # calculate the number of lowercase letters
    uppercase_letters = count_letters(text, 'uppercase')  # calculate the number of uppercase letters

    print(f'Percentage of lowercase letters: {lowercase_letters / total_letters * 100:.2f}%')
    print(f'Percentage of uppercase letters: {uppercase_letters / total_letters * 100:.2f}%')
