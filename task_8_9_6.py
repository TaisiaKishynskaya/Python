from utils import print_intro, validate_number_input

print_intro()


def main():
    year = validate_number_input(input('Enter year: '))
    massage = 'Leap year.' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 \
        else 'Ordinary year.'
    print(massage)


if __name__ == '__main__':
    main()
