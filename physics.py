import pyxel
from constants import *
import math
from enum import Enum

class Wheel(Enum):
    Front = 0
    Rear = 1

class Coordinate(Enum):
    World = 0
    Local = 1

class Vec2:
    def __init__(self):
        self.x = False
        self.y = False
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def rotate(self, radian):
        sin_a = math.sin(radian)
        cos_a = math.cos(radian)
        x1 = cos_a * self.x - sin_a * self.y
        y1 = sin_a * self.x + cos_a * self.y
        return Vec2(x1, y1)

class Location(Vec2):
    def __init__(self):
        self.coordinate = False
        self.x = False
        self.y = False

    def __init__(self, coord, x, y):
        self.coordinate = coord
        self.x = x
        self.y = y

class Bike:
    def __init__(self, image_index):
        self.width = 48
        self.height = 32
        self.wheel_radius = 8
        self.front_wheel_center = Vec2(12, 8)
        self.rear_wheel_center = Vec2(8, 8)
        self.image_index = image_index
        self.location = Vec2(ScreenSize[0] / 2, ScreenSize[1] / 2)
        self.rotation = 0 # radian
        self.load()

    def load(self):
        self.image = pyxel.images[self.image_index]
        self.image.load(0, 0, "images/bike.png")

    def set_location(self, x, y):
        self.location = Vec2(x, y)

    def to_local(self, location):
        if location.coordinate == Coordinate.Local:
            return location
        if location.coordinate != Coordinate.World:
            raise
        lxy = (location - self.location).rotate(-self.rotation)
        return Location(Coordinate.Local, lxy.x, lxy.y)

    def to_world(self, location):
        if location.coordinate == Coordinate.World:
            return location
        if location.coordinate != Coordinate.Local:
            raise
        rxy = self.location.rotate(self.rotation)
        wxy = rxy + self.location
        return Location(Coordinate.World, wxy.x, wxy.y)

    def wheel_center(self, wheel):
        if wheel == Wheel.Front:
            wcenter = self.front_wheel_center
        elif wheel == Wheel.Rear:
            wcenter = self.rear_wheel_center
        else:
            raise
        return Location(Coordinate.Local, wcenter.x, wcenter.y)
    
    def wheel_is_on_ground(self, wheel, ground):
        wcenter = self.wheel_center(wheel)
        wwcenter = self.to_world(wcenter)
        gh = ground.height(wcenter.x)
        diff = abs(gh - wwcenter.y)
        return (diff <= self.wheel_radius)
    
    def show(self):
        x = self.location.x - self.width / 2
        y = self.location.y - self.height / 2
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
    # Pyxel Initialization
    pyxel.init(100, 100)
    # Ground Test
    ground = Ground([Vec2(0.0, 1.0), Vec2(10.0, 15.0)])
    for x in range(20):
        y = ground.height(x)
        print('x: %f, y: %f' % (x, y))
    # Bike Test
    bike = Bike(0)
    bike.set_location(5.0, 20.0)
    print('Bike is on ground: %d %d' %
          (bike.wheel_is_on_ground(Wheel.Front, ground),
           bike.wheel_is_on_ground(Wheel.Rear, ground)))
    bike.set_location(5.0, 10.0)
    print('Bike is on ground: %d %d' %
          (bike.wheel_is_on_ground(Wheel.Front, ground),
           bike.wheel_is_on_ground(Wheel.Rear, ground)))
    
