import math
from enum import Enum

BikeWorldLen = 1.5 # [m]
BikeSpriteWidth = 48 # [pixel]
BikeSpriteHeight = 32 # [pixel]

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

    def __mul__(self, other):
        return Vec2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vec2(self.x / other.x, self.y / other.y)

    def __str__(self):
        return "Vec2(%f,%f)" % (self.x, self.y)

    def mul(self, other):
        return Vec2(self.x * other, self.y * other)
    
    def div(self, other):
        return Vec2(self.x / other, self.y / other)

    def rotate(self, radian):
        sin_a = math.sin(radian)
        cos_a = math.cos(radian)
        x1 = cos_a * self.x - sin_a * self.y
        y1 = sin_a * self.x + cos_a * self.y
        return Vec2(x1, y1)

class World:
    def __init__(self):
        self.second = 0
        self.delta_second = 0
        self.scale = Vec2(BikeSpriteWidth / BikeWorldLen,
                          -BikeSpriteWidth / BikeWorldLen)
        self.screen_size = Vec2(240, 180)
        self.title = "Yumia Bike Dash"
        self.bg_index = 0
        self.origin_world = Vec2(0.0, 0.0)
        self.origin_screen = Vec2(self.screen_size.x / 4,
                                  self.screen_size.y * 3 / 4)

    def screen_xy(self, world_xy):
        w_diff = world_xy - self.origin_world
        s_diff = w_diff * self.scale
        return self.origin_screen + s_diff

    def world_xy(self, screen_xy):
        s_diff = screen_xy - self.origin_screen
        w_diff = s_diff / self.scale
        return self.origin_world + w_diff

world = World()
