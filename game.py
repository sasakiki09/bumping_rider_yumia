import pyxel
from world import *
from physics import *

class GameBike:
    def __init__(self):
        self.bike = Bike()
        self.width = 48
        self.height = 32
        self.wheel_radius = 8
        self.front_wheel_center = Vec2(12, 8)
        self.rear_wheel_center = Vec2(8, 8)
        self.image_index = image_index
        self.load()

    def load(self):
        self.image = pyxel.images[self.image_index]
        self.image.load(0, 0, "images/bike.png")

    def show(self):
        return
        x = self.location.x - self.width / 2
        y = self.location.y - self.height / 2
        pyxel.blt(x, y, self.image_index,
                  0, 0, self.width, self.height,
                  BGIndex,
                  self.rotation)

class App:
    def __init__(self):
        pyxel.init(ScreenSize[0], ScreenSize[1], Title)
        self.player = Bike(0)
        self.tic = 0
        self.ground = Ground([Vec2(0.0, 10.0), Vec2(10.0, 15.0)])
        pyxel.run(self.update, self.draw)

    def update(self):
        self.tic += 1
        self.player.rotation = self.tic % 360
        self.input()

    def draw(self):
        pyxel.cls(13)
        self.player.show()

    def input(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.location.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.location.x += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.player.location.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.player.location.y += 1

App()
