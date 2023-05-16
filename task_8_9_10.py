from utils import print_intro

print_intro()


def get_position():
    while True:
        position = input('Enter the position of the chess piece (e.g. a1): ')
        if len(position) != 2 or position[0] not in 'abcdefgh' or position[1] not in '12345678':
            print('Invalid input. Please enter a letter between a-h and a number between 1-8.')
        else:
            return position[0], int(position[1])


def determine_color(let, num):
    return 'black' if (ord(let) + num) % 2 == 0 else 'white'


if __name__ == '__main__':
    letter, number = get_position()
    color = determine_color(letter, number)
    print(f'The square at {letter+str(number)} is {color}.')
