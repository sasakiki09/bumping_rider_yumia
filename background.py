import pyxel
import random
from enum import Enum, auto
from world import *
from stages import *
from color_palette import ColorPalette

class Background:
    def __init__(self):
        stage = stages[world.stage_index]
        self.time_period = stage.time_period
        random.seed(stage.seed)
        self.origin_world_x = 0.0
        self.last_index = False
        self.gen_stars()
        self.gen_mountains()
        self.gen_clouds()
    
    def bg_color(self):
        if (self.time_period == TimePeriod.Night):
            return ColorPalette.NightSky
        else:
            return ColorPalette.DaySky

    def gen_stars(self):
        min_y = 0.3
        max_y = 1.0
        count = 200
        xys = []
        for _ in range(count):
            x = random.uniform(0.0, 1.0)
            y = random.uniform(min_y, max_y)
            xys.append(Vec2(x, y))
        self.stars_xys = xys

    def gen_mountains(self):
        min_y = 0.2
        max_y = 0.9
        max_x_interval = 0.2
        self.mountains_scale = 3.0
        last_x = 0.0
        last_y = 0.5
        xys = []
        while last_x < self.mountains_scale:
            y = last_y + (random.random() - 0.5) * max_x_interval
            y = min(max(y, 0.0), 1.0)
            x = last_x + random.random() * max_x_interval
            xys.append(Vec2(x, min_y + y * (max_y - min_y)))
            last_x = x
        self.mountains_xys = xys

    def gen_clouds(self):
        min_y = 0.7
        max_y = 1.0
        min_w = 0.3
        max_w = 0.5
        min_h = 0.02
        max_h = 0.04
        count = 20
        self.clouds_scale = 5
        xys = []
        for _ in range(count):
            x = random.uniform(0.0, self.clouds_scale)
            y = random.uniform(min_y, max_y)
            v = Vec2(x, y)
            v.w = random.uniform(min_w, max_w)
            v.h = random.uniform(min_h, max_h)
            xys.append(v)
        self.clouds_xys = xys

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
        s_w = world.screen_size.x
        s_h = world.screen_size.y
        color = 7
        for v in self.stars_xys:
            sx = v.x * s_w
            sy = (1.0 - v.y) * s_h
            pyxel.pset(sx, sy, color)

    def show_mountains(self):
        color = 3
        scale = self.mountains_scale
        s_w = world.screen_size.x
        s_h = world.screen_size.y
        origin_x = self.origin_world_x * world.scale.x / s_w
        for sx in range(s_w):
            y = self.calc_y(self.mountains_xys,
                            sx / s_w + origin_x / scale,
                            scale)
            sy = (1 - y) * s_h
            pyxel.line(sx, sy, sx, s_h - 1, color)
        
    def show_clouds(self):
        color = 7
        scale = self.clouds_scale
        s_w = world.screen_size.x
        s_h = world.screen_size.y
        origin_x = self.origin_world_x * world.scale.x / s_w
        speed = 1.0 / 3.0
        for v in self.clouds_xys:
            x = v.x - origin_x
            while x * speed + v.w < 0.0:
                x += scale
            sx = x * speed * s_w
            sy = (1 - v.y) * s_h
            sw = v.w * s_w
            sh = v.h * s_h
            pyxel.rect(sx, sy, sw, sh, color)

    def show(self):
        pyxel.cls(self.bg_color())
        self.show_stars()
        self.show_mountains()
        self.show_clouds()
