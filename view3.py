from const import DRAW, PLAYER_X, PLAYER_O

import pyxel

class TicTacToeView3:
    def __init__(self):
        self.board = [
            'O', '', 'O',
            '', 'X', '',
            'X', 'O', '',
        ]
        pyxel.init(52, 52)
        # pyxel.run(self.update, self.draw)

    def draw_tokens(self, board):
        for row in range(3):
            for col in range(3):
                if board[row * 3 + col] == PLAYER_X:  # Player 1 (Red X)
                    x = col * 17 + 8
                    y = row * 17 + 8
                    pyxel.line(x - 4, y - 4, x + 4, y + 4, 8)  # Red diagonal line \
                    pyxel.line(x - 4, y + 4, x + 4, y - 4, 8)  # Red diagonal line /
                elif board[row * 3 + col] == PLAYER_O:  # Player 2 (Blue O)
                    x = col * 17 + 8
                    y = row * 17 + 8
                    pyxel.circ(x, y, 5, 12)  # Blue circle

    def draw_board_lines(self):
        # Draw the background
        pyxel.cls(7)  # Fill the screen with white (color 7)

        # Draw the grid lines
        pyxel.line(17, 0, 17, 51, 0)  # Vertical line 1
        pyxel.line(34, 0, 34, 51, 0)  # Vertical line 2
        pyxel.line(0, 17, 51, 17, 0)  # Horizontal line 1
        pyxel.line(0, 34, 51, 34, 0)  # Horizontal line 2

        # Draw the border
        pyxel.rect(0, 0, 52, 1, 0)  # Top border
        pyxel.rect(0, 51, 52, 1, 0)  # Bottom border
        pyxel.rect(0, 0, 1, 52, 0)  # Left border
        pyxel.rect(51, 0, 1, 52, 0)  # Right border

    def display_board(self, board):
        self.draw_board_lines()
        self.draw_tokens(board)

    def update(self):
        pass

    def draw(self):
        pass

# TicTacToeView3()