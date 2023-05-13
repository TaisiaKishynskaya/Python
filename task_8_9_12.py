import random
from utils import print_intro

print_intro()


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def get_user_choice():
    while True:
        choice = input('Choose rock, paper, or scissors: ')
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print('Invalid input. Please choose rock, paper, or scissors.')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    if user_choice == 'rock' and computer_choice == 'scissors':
        return 'user'
    if user_choice == 'paper' and computer_choice == 'rock':
        return 'user'
    if user_choice == 'scissors' and computer_choice == 'paper':
        return 'user'
    return 'computer'


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f'You chose {user_choice}. The computer chose {computer_choice}.')

    winner = determine_winner(user_choice, computer_choice)
    if winner == 'tie':
        print("It's a tie!")
    else:
        print(f'The {winner} wins!')


if __name__ == '__main__':
    while True:
        print("Let's play Rock, Paper, Scissors!")
        play_game()

        play_again = input('Do you want to play again? (y/n): ')
        if play_again.lower() != 'y':
            break
