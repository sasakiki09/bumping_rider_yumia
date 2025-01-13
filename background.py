import pyxel

class Background:
    def __init__(self):
        self.color_index = 7

    def show(self):
        pyxel.cls(self.color_index)
