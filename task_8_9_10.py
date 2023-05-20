from itertools import product
from utils import print_intro

print_intro()


def get_position():
    while True:
        position = input('Enter the position of the chess piece (e.g. a1): ')
        if position in (''.join(i) for i in product('abcdefgh', '12345678')):
            return position
        print('Invalid input. Please enter a letter between a-h and a number between 1-8.')


def determine_color(let, num):
    color_cell = 'black' if (ord(let) + ord(num)) % 2 else 'white'
    return color_cell


# pylint: disable=invalid-name
if __name__ == '__main__':
    letter, number = get_position()
    color = determine_color(letter, number)
    print(f'The square at {letter+str(number)} is {color}.')
