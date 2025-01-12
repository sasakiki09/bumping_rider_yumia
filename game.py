import pyxel
from world import *
from physics import *

class GameBike:
    def __init__(self, image_index):
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

    def screen_xy(self):
        w_loc = self.bike.get_location()
        return world.screen_xy(w_loc)

    def set_rotation(self, rot):
        self.bike.rotation = rot

    def add_xy(self, xy):
        self.bike.location += xy
    
    def rotation_degree(self):
        rotation = self.bike.rotation
        return 180.0 / math.pi * rotation
        
    def show(self):
        s_xy = self.screen_xy()
        rot = self.rotation_degree()
        pyxel.blt(s_xy.x, s_xy.y, self.image_index,
                  0, 0, self.width, self.height,
                  world.bg_index,
                  rot)

class GameGround:
    def __init__(self, coords):
        self.ground = Ground(coords)
        self.color = 1

    def screen_y(self, screen_x):
        w_xy = world.world_xy(Vec2(screen_x, 0))
        w_y = self.ground.height(w_xy.x)
        if not w_y: return False
        s_xy = world.screen_xy(Vec2(w_xy.x, w_y))
        return s_xy.y

    def show(self):
        for x in range(world.screen_size.x):
            y = self.screen_y(x)
            if y:
                pyxel.line(x, y, x, world.screen_size.y, self.color)

class App:
    def __init__(self):
        pyxel.init(world.screen_size.x,
                   world.screen_size.y,
                   world.title)
        self.bike = GameBike(0)
        self.tic = 0
        self.ground = GameGround([Vec2(0.0, 10.0), Vec2(10.0, 15.0)])
        pyxel.run(self.update, self.draw)

    def update(self):
        self.tic += 1
        deg = math.pi / 180 * (self.tic % 360)
        self.bike.set_rotation(deg)
        self.input()

    def draw(self):
        pyxel.cls(13)
        self.bike.show()
        self.ground.show()

    def input(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.bike.add_xy(Vec2(-1, 0))
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.bike.add_xy(Vec2(1, 0))
        if pyxel.btn(pyxel.KEY_UP):
            self.bike.add_xy(Vec2(0, -1))
        if pyxel.btn(pyxel.KEY_DOWN):
            self.bike.add_xy(Vec2(0, 1))

App()
