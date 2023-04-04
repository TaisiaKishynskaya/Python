def get_guest_name():
    while True:
        try:
            your_name = input('Guest name: ')
            if not your_name.isalpha() and not your_name.isspace():
                raise ValueError('Name should only contain letters and spaces.')
            return your_name
        except KeyboardInterrupt:
            print('Program interrupted by user.')
            return 'q'
        except ValueError as err:
            print(err)


def write_guest_name_to_file(the_filename, the_name):
    try:
        with open(the_filename, 'a', encoding='utf-8') as the_file_object:
            the_file_object.write(f'{the_name.title()} visited our event.\n')
    except IOError:
        print(f'Error writing to file {the_filename}.')


if __name__ == '__main__':
    FILE_NAME = 'guest_book.txt'

    print('Enter guest names.')
    print('Enter "q" to quit.')

    while True:
        name = get_guest_name()
        if name == 'q':
            break
        print(f'Welcome, {name.title()}!')
        write_guest_name_to_file(FILE_NAME, name)
