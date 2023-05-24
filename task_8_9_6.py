from utils import print_intro, get_valid_number_input

print_intro()


def main():
    year = get_valid_number_input('Enter year: ', int)
    massage = 'Leap year.' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0\
        else 'Ordinary year.'
    return massage


if __name__ == '__main__':
    print(main())
