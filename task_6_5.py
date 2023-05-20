FILE_NAME = 'guest_book.txt'


def collect_guest_names(the_filename):
    with open(the_filename, 'a', encoding='utf-8') as the_file_object:
        while True:
            name = input('Guest name: ')
            if name == 'q':
                break
            print(f'Welcome, {name.title()}!')
            the_file_object.write(f'{name.title()} visited our event.\n')


if __name__ == '__main__':
    print('Enter guest names.')
    print('Enter "q" to quit.')
    collect_guest_names(FILE_NAME)
