import sys
from utils import print_intro

print_intro()


def validate_input(my_num):
    if my_num.isdigit() and len(my_num) == 6:
        return my_num
    return None


def check_lucky_num(num):
    if num is not None:
        result = 'lucky' if sum(map(int, num[:3])) == sum(map(int, num[3:])) else 'unlucky'
        print(f'This number is {result}')
    else:
        print('Input six-digit number!')


if __name__ == '__main__':
    while True:
        input_data = input('Input six-digit number or type "exit" to quit: ')
        valid_num = validate_input(input_data)
        check_lucky_num(valid_num)

        if str(input_data).lower() == 'exit':
            sys.exit()
