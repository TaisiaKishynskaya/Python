from utils import print_intro
print_intro()


def input_number():
    my_num = input('Input six-digit number or type "exit" to quit: ')
    if my_num.isdigit() and len(my_num) == 6:
        return int(my_num)
    else:
        return None


if __name__ == '__main__':
    while True:
        my_num = input_number()

        if my_num is None:
            print('Input six-digit number!')
        else:
            RESULT = 'lucky' if sum(map(int, str(my_num)[:3])) == sum(map(int, str(my_num)[3:])) else 'unlucky'
            print(f'This number is {RESULT}')
        if str(my_num).lower() == 'exit':
            break

    print(my_num)



"""def input_number():
    my_num = input('Input six-digit number or type "exit" to quit: ')
    try:
        my_num = int(my_num)
    except ValueError:
        pass
    return my_num


if __name__ == '__main__':
    while True:
        my_str = input_number()

        if len(str(my_str)) == 6:
            RESULT = 'lucky' if sum(map(int, str(my_str)[:3])) == sum(map(int, str(my_str)[3:])) else 'unlucky'
            print(f'This number is {RESULT}')
        elif str(my_str).lower() == 'exit':
            break
        elif not isinstance(my_str, int):
            print('Input number!')
            input_number()
        else:
            print('Input six-digit number!')

    print(my_str)"""
