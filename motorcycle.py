import pyxel

ScreenSize = [240, 180]
Title = "Yumia Motor Dash"

class Player:
    def __init__(self, image_index):
        self.width = 48
        self.height = 32
        self.image_index = image_index
        self.x = ScreenSize[0] / 2
        self.y = ScreenSize[1] / 2
        self.load()

    def load(self):
        pyxel.images[self.image_index].load(0, 0, "images/player.png")

    def show(self):
        x = self.x - self.width / 2
        y = self.y - self.height / 2
        pyxel.blt(x, y, self.image_index,
                  0, 0, self.width, self.height, 0)

class App:
    def __init__(self):
        pyxel.init(ScreenSize[0], ScreenSize[1], Title)
        self.player = Player(0)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.input()

    def draw(self):
        pyxel.cls(13)
        self.player.show()

    def input(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.x += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.player.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.player.y += 1

App()

