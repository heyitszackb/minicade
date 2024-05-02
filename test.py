import pyxel

class Model:
    def __init__(self):
        self.board = [0] * 9
        self.current_player = 1

    def make_move(self, position):
        if self.board[position] == 0:
            self.board[position] = self.current_player
            self.current_player = 2 if self.current_player == 1 else 1

    def check_winner(self):
        winning_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]
        for pos in winning_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != 0:
                return self.board[pos[0]]
        if 0 not in self.board:
            return -1  # Draw
        return 0

    def reset(self):
        self.board = [0] * 9
        self.current_player = 1

class View:
    def __init__(self):
        pyxel.init(120, 120)
        self.cell_size = 40
        self.colors = [1, 2, 3, 4]  # Define the colors for animation
        self.frame_count = 0
        self.drawing_progress = {}
        self.drawing_speed = 2  # Adjust the drawing speed as needed

    def update(self): # view update doesn't actually draw anything, just necessary for INTERNAL VIEW LOGIC
        self.frame_count += 1
        for position in self.drawing_progress.keys():
            if self.drawing_progress[position] < 100:
                self.drawing_progress[position] += self.drawing_speed

    def draw(self, board, winner): # this is the only function that actually draws things. Draws state based on internal logic of the view code (processed by the view update)
        pyxel.cls(7)
        self.draw_board()
        self.draw_pieces(board)
        if winner != 0:
            self.draw_winner(winner)


    def draw_board(self):
        pyxel.line(40, 0, 40, 120, 0)
        pyxel.line(80, 0, 80, 120, 0)
        pyxel.line(0, 40, 120, 40, 0)
        pyxel.line(0, 80, 120, 80, 0)

    def draw_pieces(self, board):
        for i in range(9):
            if board[i] != 0 and i not in self.drawing_progress:
                self.drawing_progress[i] = 0

            if board[i] == 1:
                self.draw_x(i)
            elif board[i] == 2:
                self.draw_o(i)

    def draw_x(self, position):
        x = (position % 3) * self.cell_size + 10
        y = (position // 3) * self.cell_size + 10
        color = self.colors[self.frame_count % len(self.colors)]
        progress = self.drawing_progress.get(position, 100) / 100

        if progress < 0.5:
            x1 = x
            y1 = y
            x2 = x + int(20 * progress * 2)
            y2 = y + int(20 * progress * 2)
            pyxel.line(x1, y1, x2, y2, color)
            pyxel.line(x + 20, y, x + 20 - int(20 * progress * 2), y + int(20 * progress * 2), color)
        else:
            x1 = x
            y1 = y
            x2 = x + 20
            y2 = y + 20
            pyxel.line(x1, y1, x2, y2, color)
            pyxel.line(x + 20, y, x, y + 20, color)

    def draw_o(self, position):
        x = (position % 3) * self.cell_size + 20
        y = (position // 3) * self.cell_size + 20
        color = self.colors[self.frame_count % len(self.colors)]
        progress = self.drawing_progress.get(position, 100) / 100

        radius = int(10 * progress)
        pyxel.circ(x, y, radius, color)

    def draw_winner(self, winner):
        pyxel.text(50, 50, "Player {} wins!".format(winner), 0)

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        pyxel.run(self.update, self.draw)

    def process_user_actions(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            x = pyxel.mouse_x // 40
            y = pyxel.mouse_y // 40
            position = y * 3 + x
            self.model.make_move(position)
        if pyxel.btnp(pyxel.KEY_R):
            self.model.reset()

    def update(self): # executed each frame
        # process actions:
        self.process_user_actions()
        self.view.update() # executed each frame

    def draw(self): # executed each frame 
        winner = self.model.check_winner()
        self.view.draw(self.model.board, winner) # executed each frame

if __name__ == "__main__":
    controller = Controller()
    controller.run()