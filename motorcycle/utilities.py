import pyxel
import math
import time

import pdb

def blt_center(cx, cy, img, u, v, w, h, colkey, rotate = 0, scale = 1):
    x = cx - w / 2
    y = cy - h / 2
    pyxel.blt(x, y, img, u, v, w, h, colkey, rotate, scale)

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

class Vec2Array:
    def __init__(self, array):
        self.array = sorted(array, key=lambda c: c.x)
        if len(self.array) < 2:
            pdb.set_trace()
            raise
        count = len(self.array) - 1
        x_len = self.array[-1].x - self.array[0].x
        self.diff_x_avg = x_len / count
        self.inv_array = self._calc_inv_array()

    # Calculate index s.t.
    #   array[index] <= floor(diff_x / diff_x_avg).
    def _calc_inv_array(self):
        inv_array = []
        for index in range(len(self.array)):
            diff_x = self.array[index].x - self.array[0].x
            while len(inv_array) <= math.floor(diff_x / self.diff_x_avg):
                inv_array.append(index)
        return inv_array

    def __str__(self):
        astr = "array: ["
        for xy in self.array:
            astr += str(xy) + ", "
        astr += "], "
        astr += "diff_x_ang: " + str(self.diff_x_avg) + ", "
        astr += "inv_array: " + str(self.inv_array)
        return astr

    # Find minimum index such that xys[index] <= x.
    def find_index(self, x):
        n = len(self.array)
        i = math.floor((x - self.array[0].x) / self.diff_x_avg)
        if i < 0: return 0
        if i >= len(self.inv_array): return n - 1
        index = self.inv_array[i]
        while index < n and self.array[index].x <= x:
            index += 1
        return index - 1

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

class ImageUtils:
    def __init__(self, image, range = None):
        self.image = image
        if not range:
            range = Range2(0, 0, image.width, image.height)
        self.range = range

    def clipped(self, converter = None):
        image = pyxel.Image(self.range.w, self.range.h)
        for y in range(self.range.h):
            for x in range(self.range.w):
                c = self.image.pget(self.range.x + x, self.range.y + y)
                if converter:
                    c = converter(c)
                image.pset(x, y, c)
        return image
