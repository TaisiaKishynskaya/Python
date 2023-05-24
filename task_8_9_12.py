import random
from utils import print_intro

print_intro()


ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
CHOISES = [ROCK, PAPER, SCISSORS]
WIN_COMBINATIONS = ((ROCK, SCISSORS), (PAPER, ROCK), (SCISSORS, PAPER))
TIE = 'tie'


def get_user_choice():
    while True:
        choice = input('Choose rock, paper, or scissors: ')
        if choice in CHOISES:
            return choice
        print('Invalid input. Please choose rock, paper, or scissors.')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return TIE
    if (user_choice, computer_choice) in WIN_COMBINATIONS:
        return 'user'
    return 'computer'


def play_game():
    user_choice = get_user_choice()
    computer_choice = random.choice(CHOISES)

    print(f'You chose {user_choice}. The computer chose {computer_choice}.')

    winner = determine_winner(user_choice, computer_choice)
    massage = f"It's a {TIE}!" if winner == TIE else f'The {winner} wins!'
    print(massage)


if __name__ == '__main__':
    while True:
        print("Let's play Rock, Paper, Scissors!")
        play_game()

        play_again = input('Do you want to play again? (y/n): ')
        if play_again.lower() != 'y':
            break
