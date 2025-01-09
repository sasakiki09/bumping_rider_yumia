import pyxel
from constants import *
from physics import *

class App:
    def __init__(self):
        pyxel.init(ScreenSize[0], ScreenSize[1], Title)
        self.player = Player(0)
        self.tic = 0
        self.ground = Ground([Vec2(0.0, 10.0), Vec2(10.0, 15.0)])
        pyxel.run(self.update, self.draw)

    def update(self):
        self.tic += 1
        self.player.rotation = self.tic % 360
        self.input()
        self.test()

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

    def test(self):
        x = self.tic
        y = self.ground.height(x)
        print('x: %f, y: %f' % (x, y))

App()
