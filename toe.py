from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    TITLE = 'Tic Tac Toe!'
    BUTTON_IDS = ['btn1', 'btn2', 'btn3', 'btn4', 'btn5', 'btn6', 'btn7', 'btn8', 'btn9']

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        return Builder.load_file('toe.kv')

    turn = 'X'  # Define Who's turn it is
    winner = False  # Keep track of win or lose

    # No winner
    def no_winner(self):
        if self.winner is False and all(self.root.ids[button_id].disabled for button_id in self.BUTTON_IDS):
            self.root.ids.score.text = "IT'S A TIE!"

    # End the Game
    def end_game(self, val_a, val_b, val_c):
        self.winner = True
        val_a.color = val_b.color = val_c.color = 'red'
        self.disable_all_buttons()  # Disable the buttons
        self.root.ids.score.text = f'{val_a.text} Wins!'  # Set label for winner

        # Keep track of winners or losers
        wins = {'X': 0, 'O': 0}
        if val_a.text in wins:
            wins[val_a.text] += 1
        self.root.ids.game.text = f'X Wins: {wins["X"]} | O Wins: {wins["O"]}'

    def disable_all_buttons(self):
        # Disable the buttons
        for b_id in range(1, 10):
            self.root.ids[f'btn{b_id}'].disabled = True

    def win(self):
        lines = [[self.root.ids[f'btn{button_id}'] for button_id in range(1, 4)],  # Across (1st row)
                 [self.root.ids[f'btn{button_id}'] for button_id in range(4, 7)],  # Across (2nd row)
                 [self.root.ids[f'btn{button_id}'] for button_id in range(7, 10)],  # Across (3rd row)
                 [self.root.ids[f'btn{button_id}'] for button_id in range(1, 10, 3)],  # Down (1st column)
                 [self.root.ids[f'btn{button_id}'] for button_id in range(2, 10, 3)],  # Down (2nd column)
                 [self.root.ids[f'btn{button_id}'] for button_id in range(3, 10, 3)],  # Down (3rd column)
                 [self.root.ids[f'btn{button_id}'] for button_id in range(1, 10, 4)],  # Diagonal (top-left to bottom-r)
                 [self.root.ids[f'btn{button_id}'] for button_id in range(3, 8, 2)]]  # Diagonal (top-r to bottom-left)
        for line in lines:
            if line[0].text != '' and all(btn.text == line[0].text for btn in line):
                self.end_game(*line)
                return
        self.no_winner()

    def presser(self, btn):
        if self.turn == 'X':
            btn.text = 'X'
            btn.disabled = True
            self.root.ids.score.text = "O's Turn!"
            self.turn = 'O'
        else:
            btn.text = 'O'
            btn.disabled = True
            self.root.ids.score.text = "X's Turn!"
            self.turn = 'X'
        self.win()  # Check to see if won

    def restart(self):
        self.turn = 'X'  # Reset Who`s turn it is

        for button_id in range(1, 10):
            self.root.ids[f'btn{button_id}'].disabled = False  # Enable the buttons
            self.root.ids[f'btn{button_id}'].text = ''  # Clear the buttons
            self.root.ids[f'btn{button_id}'].color = 'green'  # Reset the buttons colors

        self.root.ids.score.text = 'X GOES FIRST!'  # Reset the score Label
        self.winner = False  # Reset rhe winner variable


MainApp().run()
