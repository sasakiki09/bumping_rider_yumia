import math
from enum import Enum

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
        self.scale = 48 / 170.0
        self.screen_size = Vec2(240, 180)
        self.title = "Yumia Bike Dash"
        self.bg_index = 0
        self.origin_world = Vec2(0.0, 0.0)
        self.origin_screen = self.screen_size.div(2.0)

world = World()
