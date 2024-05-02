import pyxel

from const import PLAYER_X, PLAYER_O, DRAW

from model import Model

class View:
    def __init__(self):
        pyxel.init(98, 98)
        pyxel.load("tictactwo.pyxres")
        self.cell_size = 32
    def update(self): # view update doesn't actually draw anything, just necessary for INTERNAL VIEW LOGIC
        pass

    def draw(self, model: Model): # this is the only function that actually draws things. Draws state based on internal logic of the view code (processed by the view update)
        pyxel.cls(7)
        self.draw_board()
        self.draw_pieces(model.get_board())
        winner = model.get_is_game_over()
        if winner != '':
            self.draw_winner(winner)


    def draw_board(self):
        pyxel.line(33, 0, 33, 98, 0)
        pyxel.line(66, 0, 66, 98, 0)
        pyxel.line(0, 33, 98, 33, 0)
        pyxel.line(0, 66, 98, 66, 0)

    def draw_pieces(self, board):
        for i in range(9):
            if board[i] == PLAYER_X:
                self.draw_x(i)
            elif board[i] == PLAYER_O:
                self.draw_o(i)

    def draw_x(self, position):
        x = (position % 3) * self.cell_size + 9
        y = (position // 3) * self.cell_size + 9
        
        pyxel.blt(x, y, 0, 0, 0, 16, 16, pyxel.COLOR_BLACK)

    def draw_o(self, position):
        x = (position % 3) * self.cell_size + 9
        y = (position // 3) * self.cell_size + 9
        pyxel.blt(x, y, 0, 16, 0, 16, 16, pyxel.COLOR_BLACK)

    def draw_winner(self, winner):
        pass
        # if winner == DRAW, should display the text "there is a draw, press R to restart"
        # if winner == PLAYER_X, should display a line through the winning combination in red
        # if winner == PLAYER_O, should display a line through the winning combination in blue

        # use model.get_winning_combination() to get the winning combination, consider the following code from chat.lmsys:

        '''
        if winner == DRAW:
            pyxel.text(10, 50, "There is a draw, press R to restart", pyxel.COLOR_BLACK)
        else:
            winning_combination = self.model.get_winning_combination()
            if winning_combination:
                start_x = (winning_combination[0] % 3) * self.cell_size + 16
                start_y = (winning_combination[0] // 3) * self.cell_size + 16
                end_x = (winning_combination[2] % 3) * self.cell_size + 16
                end_y = (winning_combination[2] // 3) * self.cell_size + 16

                color = pyxel.COLOR_RED if winner == PLAYER_X else pyxel.COLOR_BLUE
                pyxel.line(start_x, start_y, end_x, end_y, color)
        '''