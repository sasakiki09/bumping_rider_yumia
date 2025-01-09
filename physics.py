import pyxel
from constants import *
import math
from enum import Enum

class WheelType(Enum):
    Front = 0
    Rear = 1

class Coordinate(Enum):
    World = 0
    Chara = 1

class Vec2:
    def __init__(self):
        self.x = False
        self.y = False
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

class Location(Vec2):
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
        self.location = Vec2(ScreenSize[0] / 2, ScreenSize[1] / 2)
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

    def wheel_center(self, wheel):
        if wheel == Wheel.Front:
            wcenter = self.front_wheel_center
        elif wheel == WheelRear:
            wcenter = self.rear_wheel_center
        else:
            raise
        r_center = self.rotate(wcenter)
    
    def wheel_is_on_ground(self, wheel, ground):
        
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
        self.last_index = False

    def __init__(self, coords):
        self.coords = sorted(coords, key=lambda c: c.x)
        if len(self.coords) < 2: raise
        self.last_index = False

    # Find minmum index such that self.coords[index] <= x.
    def find_index(self, x):
        if not self.last_index: self.last_index = 0
        index = self.last_index
        while (index < len(self.coords) - 1 and
               self.coords[index].x < x):
            index += 1
        while (0 < index and
               x < self.coords[index].x):
            index -= 1
        return index
        
    def height(self, x):
        index = self.find_index(x)
        if index == len(self.coords) - 1:
            return self.coords[index].y
        x0 = self.coords[index].x
        y0 = self.coords[index].y
        x1 = self.coords[index + 1].x
        y1 = self.coords[index + 1].y
        if not (x0 <= x and x <= x1): raise
        if x0 == x1: raise
        return y0 + (y1 - y0) / (x1 - x0) * (x - x0)

if __name__ == '__main__':
    ground = Ground([Vec2(0.0, 1.0), Vec2(10.0, 15.0)])
    for x in range(20):
        y = ground.height(x)
        print('x: %f, y: %f' % (x, y))

