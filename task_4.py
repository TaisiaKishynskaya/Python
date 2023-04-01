def input_number():
    my_num = input('Input six-digit number or type "exit" to quit: ')
    try:
        my_num = int(my_num)
    except ValueError:
        pass
    return my_num


if __name__ == '__main__':
    from utils import get_intro_string, get_name_string

    print(get_intro_string())
    print(get_name_string())

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

    print(my_str)
