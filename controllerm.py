from modelm import TicTacToe
from viewm import TicTacToeView
from view3 import TicTacToeView3

class TicTacToeController:
    def __init__(self):
        self.model = TicTacToe()
        self.view = TicTacToeView()
        self.view3 = TicTacToeView3()


    def play(self):
        while not self.model.get_is_game_over():
            # self.view.display_board(self.model.get_board())
            self.view3.display_board(self.model.get_board())
            current_player = self.model.get_current_player()
            move = self.view.get_player_move(current_player)

            if not self.model.make_move(move):
                self.view.display_invalid_move()
                continue

        self.view.display_board(self.model.get_board())
        winner = self.model.get_winning_player()
        self.view.display_winner(winner)
        self.view.display_game_over()