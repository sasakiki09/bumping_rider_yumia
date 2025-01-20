import pyxel
import random
from enum import Enum, auto
from world import *

class TimePeriod(Enum):
    Morning = auto()
    Day = auto()
    Evening = auto()
    Night = auto()

class Background:
    def __init__(self, time_period, seed):
        random.seed(seed)
        self.time_period = time_period
        self.color_index = self.color_index()
        self.origin_world_x = 0.0
        self.last_index = False
        self.gen_stars()
        self.gen_mountains()
        self.gen_clouds()

    def color_index(self):
        if (self.time_period == TimePeriod.Night):
            return 13
        else:
            return 6

    def gen_stars(self):
        pass

    def gen_mountains(self):
        min_h = 0.2
        max_h = 0.9
        max_x_interval = 0.2
        self.mountains_scale = 3.0
        last_x = 0.0
        last_y = 0.5
        xys = []
        while last_x < self.mountains_scale:
            y = last_y + (random.random() - 0.5) * max_x_interval
            y = min(max(y, 0.0), 1.0)
            x = last_x + random.random() * max_x_interval
            xys.append(Vec2(x, min_h + y * (max_h - min_h)))
            last_x = x
        self.mountains_xys = xys

    def gen_clouds(self):
        pass

    def update(self, origin_world_x):
        self.origin_world_x = origin_world_x

    def calc_y(self, xys, x, scale):
        x = x % scale
        i0 = Vec2.find_index(xys, x, self.last_index)
        i1 = (i0 + 1) % len(xys)
        x0 = xys[i0].x % scale
        y0 = xys[i0].y
        x1 = xys[i1].x % scale
        y1 = xys[i1].y
        return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    def show_stars(self):
        if self.time_period != TimePeriod.Night:
            return
        #################### TODO: implement

    def show_mountains(self):
        color = 3
        scale = self.mountains_scale
        origin_x = self.origin_world_x / world.scale.x
        sw = world.screen_size.x
        sh = world.screen_size.y
        for sx in range(sw):
            y = self.calc_y(self.mountains_xys,
                            sx / sw + origin_x / scale,
                            scale)
            sy = (1 - y) * sh
            pyxel.line(sx, sy, sx, sh - 1, color)
        
    def show_clouds(self):
        pass

    def show(self):
        pyxel.cls(self.color_index)
        self.show_stars()
        self.show_mountains()
        self.show_clouds()
