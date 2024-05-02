import pyxel
from Model.main import Model
from View.main import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self): # executed each frame
        # process actions:
        if pyxel.btnp(pyxel.KEY_0):
            print("0")
            self.model.make_move(0)
        if pyxel.btnp(pyxel.KEY_1):
            self.model.make_move(1)
        if pyxel.btnp(pyxel.KEY_2):
            self.model.make_move(2)
        if pyxel.btnp(pyxel.KEY_3):
            self.model.make_move(3)
        if pyxel.btnp(pyxel.KEY_4):
            self.model.make_move(4)
        if pyxel.btnp(pyxel.KEY_5):
            self.model.make_move(5)
        if pyxel.btnp(pyxel.KEY_6):
            self.model.make_move(6)
        if pyxel.btnp(pyxel.KEY_7):
            self.model.make_move(7)
        if pyxel.btnp(pyxel.KEY_8):
            self.model.make_move(8)
        if pyxel.btnp(pyxel.KEY_R):
            self.model.reset()
            print("RESET")
            print(self.model.get_board())


        self.view.update() # executed each frame

    def draw(self): # executed each frame
        self.view.draw(self.model) # executed each frame
        print(self.model.get_board())