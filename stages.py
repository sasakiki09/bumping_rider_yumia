import math
from world import *
from physics import *

class Stage:
    def __init__(self, xy_array):
        self.ground = self.gen_ground(xy_array)

    def gen_ground(self, xy_array):
        l = len(xy_array)
        if l % 2 != 0: raise
        vec2_array = []
        for index in range(l // 2):
            x = xy_array[index * 2 + 0]
            y = xy_array[index * 2 + 1]
            vec2_array.append(Vec2(x, y))
        return Ground(vec2_array)

stages = []

# stage 1
xys = [ -3.0, 0.0,
        5.0, 1.0,
        20.0, 0.0,
        100.0, 1.0]
stages.append(Stage(xys))
