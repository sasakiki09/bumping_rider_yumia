import pyxel
import math
from enum import Enum

ScreenSize = [240, 180]
Title = "Yumia Motor Dash"
BGIndex = 0

class WheelType(Enum):
    Front = 0
    Rear = 1

class Coordinate(Enum):
    World = 0
    Chara = 1

class Location:
    def __init__(self):
        self.coordinate = False
        self.x = False
        self.y = False

    def __init__(self, coord, x, y):
        self.coordinate = coord
        self.x = x
        self.y = y

class Player:
    def __init__(self, image_index):
        self.width = 48
        self.height = 32
        self.wheel_radius = 8
        self.front_wheel_center = [12, 8]
        self.rear_wheel_center = [8, 8]
        self.image_index = image_index
        self.x = ScreenSize[0] / 2
        self.y = ScreenSize[1] / 2
        self.rotation = 0
        self.load()

    def load(self):
        self.image = pyxel.images[self.image_index]
        self.image.load(0, 0, "images/player.png")


    def rotate(self, position):
        radian = self.rotation * math.pi / 180
        sin_a = math.sin(radian)
        cos_a = math.cos(radian)
        x1 = cos_a * position[0] - sin_a * position[1]
        y1 = sin_a * poistion[0] + cos_a * position[1]
        return [x1, y1]
        
    def wheel_is_on_ground(self, wheel, ground):
        if wheel == Wheel.Front:
            wcenter = self.front_wheel_center
        elif wheel == WheelRear:
            wcenter = self.rear_wheel_center
        else:
            raise
        r_center = self.rotate(wcenter)
        #################### working 2025.01.06
    
    def show(self):
        x = self.x - self.width / 2
        y = self.y - self.height / 2
        pyxel.blt(x, y, self.image_index,
                  0, 0, self.width, self.height,
                  BGIndex,
                  self.rotation)

class Ground:
    def __init__(self):
        self.coords = []

    def __init__(self, coords):
        self.coords = sorted(coords, key=lambda c: c[0])

    # Find minmum index such that self.coords[index] <= x.
    def find_index(self, x):
        if not self.last_index: self.last_index = 0
        index = self.last_index
        while (index < len(self.coords) and
               self.coords[index].x < x):
            index += 1
        while (0 <= index and
               x < self.coords[index].x):
            index -= 1
        return index
        
    def height(self, x):
        index = find_index(x)
        if index == len(self.coords) - 1:
            return self.coords[index].y
    #################### working 2025.01.07

class App:
    def __init__(self):
        pyxel.init(ScreenSize[0], ScreenSize[1], Title)
        self.player = Player(0)
        self.tic = 0
        self.ground = Ground([[0, 10], [10, 10]])
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
            self.player.x -= 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.x += 1
        if pyxel.btn(pyxel.KEY_UP):
            self.player.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN):
            self.player.y += 1

App()

