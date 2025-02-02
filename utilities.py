import math
import time

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

    # Find minmum index such that xys[index] <= x.
    @classmethod
    def find_index(self, xys, x, last_index = False):
        if last_index:
            index = last_index
        else:
            index = len(xys) // 2
        while (index < len(xys) - 1 and
               xys[index].x < x):
            index += 1
        while (0 < index and
               x < xys[index].x):
            index -= 1
        return index
    
class Range2:
    def __init__(self):
        self.x = None
        self.y = None
        self.w = None
        self.h = None

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
