import sys
from utils import print_intro

print_intro()


def validation(my_num):
    if my_num.isdigit() and len(my_num) == 6:
        return my_num
    return None


if __name__ == '__main__':
    while True:
        input_data = input('Input six-digit number or type "exit" to quit: ')

        valid_num = validation(input_data)

        if valid_num is None:
            print('Input six-digit number!')
        else:
            RESULT = 'lucky' if sum(map(int, valid_num[:3])) == sum(map(int, valid_num[3:])) else 'unlucky'
            print(f'This number is {RESULT}')

        if str(input_data).lower() == 'exit':
            sys.exit()
