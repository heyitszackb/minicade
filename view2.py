import pyxel

class TicTacToeView:
    def __init__(self):
        pyxel.init(120, 120)
        self._cell_size = 40
        self._board_offset = 10
        self.controller = None
        self.run()

    def _draw_board(self):
        for i in range(2):
            pyxel.line(self._board_offset, self._board_offset + (i + 1) * self._cell_size,
                       self._board_offset + 3 * self._cell_size, self._board_offset + (i + 1) * self._cell_size, 7)
            pyxel.line(self._board_offset + (i + 1) * self._cell_size, self._board_offset,
                       self._board_offset + (i + 1) * self._cell_size, self._board_offset + 3 * self._cell_size, 7)

    def _draw_mark(self, mark, row, col):
        if mark == 'X':
            self._draw_x(row, col)
        elif mark == 'O':
            self._draw_o(row, col)

    def _draw_x(self, row, col):
        x = self._board_offset + col * self._cell_size
        y = self._board_offset + row * self._cell_size
        pyxel.line(x + 5, y + 5, x + self._cell_size - 5, y + self._cell_size - 5, 10)
        pyxel.line(x + self._cell_size - 5, y + 5, x + 5, y + self._cell_size - 5, 10)

    def _draw_o(self, row, col):
        x = self._board_offset + col * self._cell_size + self._cell_size // 2
        y = self._board_offset + row * self._cell_size + self._cell_size // 2
        pyxel.circ(x, y, self._cell_size // 2 - 5, 9)

    def _draw_message(self, message):
        pyxel.text(10, 10, message, 7)

    def display_board(self, board):
        pyxel.cls(0)
        self._draw_board()
        for i in range(9):
            row, col = divmod(i, 3)
            self._draw_mark(board[i], row, col)

    def get_player_move(self, player):
        self._draw_message(f"Player {player}, click on a cell")
        while True:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                col = (pyxel.mouse_x - self._board_offset) // self._cell_size
                row = (pyxel.mouse_y - self._board_offset) // self._cell_size
                if 0 <= col < 3 and 0 <= row < 3:
                    return row * 3 + col

    def display_winner(self, winner):
        if winner == 'DRAW':
            self._draw_message("It's a draw!")
        else:
            self._draw_message(f"Player {winner} wins!")

    def display_invalid_move(self):
        self._draw_message("Invalid move. Please try again.")

    def display_game_over(self):
        self._draw_message("Game over.")

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if not self.controller.model.get_is_game_over():
            current_player = self.controller.model.get_current_player()
            move = self.get_player_move(current_player)
            self.controller.model.make_move(move)

    def draw(self):
        self.display_board(self.controller.model.get_board())
        winner = self.controller.model.get_winning_player()
        if winner:
            self.display_winner(winner)
            self.display_game_over()
        pyxel.text(10, pyxel.height - 10, "Press Q to quit", 7)