from utils import print_intro

print_intro()


def get_position():
    while True:
        position = input('Enter the position of the chess piece (e.g. a1): ')
        if len(position) == 1:
            print('Invalid input. Please enter both a letter between a-h and a number between 1-8.')
            continue

        column = position[0]  # letter
        row = position[1]  # number

        # Check if the values are within the allowed limits
        if column not in 'abcdefgh' or row not in '12345678':
            print('Invalid input. Please enter a letter between a-h and a number between 1-8.')
        else:
            return column, row


def determine_color(let, num):
    if (ord(let) + int(num)) % 2 == 0:
        return 'black'
    return 'white'


if __name__ == '__main__':
    # pylint: disable=invalid-name
    letter, number = get_position()
    color = determine_color(letter, number)
    print(f'The square at {letter+number} is {color}.')
