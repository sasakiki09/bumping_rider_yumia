import math
import random
from world import *
from savedata import *
from physics import *

class TimePeriod(Enum):
    Day = auto()
    Night = auto()

class Stage:
    def __init__(self,
                 xy_array,
                 time_period,
                 music,
                 seed,
                 x_diff_max = None,
                 y_diff_max = None):
        if x_diff_max and y_diff_max:
            self.ground = self.gen_ground_random(
                xy_array,
                x_diff_max,
                y_diff_max,
                seed)
        else:
            self.ground = self.gen_ground(xy_array)
        self.time_period = time_period
        self.music = music
        self.seed = seed
        self.best_time = None
        self.last_time = None
        
    def gen_ground(self, xy_array):
        l = len(xy_array)
        if l % 2 != 0: raise
        vec2_array = []
        for index in range(l // 2):
            x = xy_array[index * 2 + 0]
            y = xy_array[index * 2 + 1]
            vec2_array.append(Vec2(x, y))
        return Ground(vec2_array)

    def gen_ground_random(self,
                          xy_array,
                          x_diff_max,
                          y_diff_max,
                          seed):
        base_g = self.gen_ground(xy_array)
        x = xy_array[0]
        y = xy_array[1]
        random.seed(seed)
        last_base_y = y
        vec2_array = []
        while x < base_g.goal_x():
            x_diff = random.uniform(0.0, x_diff_max)
            y_diff = random.uniform(-y_diff_max, y_diff_max)
            x += x_diff
            base_y = base_g.height(x)
            y += (base_y - last_base_y) + y_diff
            vec2_array.append(Vec2(x, y))
            last_base_y = base_y
        return Ground(vec2_array)

    def start(self):
        if self.best_time == None:
            self.best_time = g_savedata.time(g_world.stage_index)

    def update_best_time(self, time):
        self.last_time = time
        if self.best_time == None:
            self.best_time = time
        else:
            self.best_time = min(self.best_time, time)
        g_savedata.set_time(g_world.stage_index, self.best_time)

g_stages = []

# stage 1
g_stages.append(Stage([ -3.0, 0.0,
                      5.0, 1.0,
                      20.0, 0.0,
                      100.0, 1.0],
                    TimePeriod.Day,
                    0,
                    0))

# stage 2
g_stages.append(Stage([ -3, 0,
                      10, 1,
                      20, 5,
                      20.1, 0,
                      50, 2,
                      100, 2],
                    TimePeriod.Night,
                    2,
                    1))

# stage 3
g_stages.append(Stage([-3, 0, 200, 0],
                      TimePeriod.Day,
                      3,
                      100,
                      0.2,
                      0.05))

# stage 4
g_stages.append(Stage([ -3, 0,
                        10, 1,
                        20, 5,
                        20.1, -5,
                        27.5, -5,
                        27.6, 2,
                        30, 0,
                        100, 4,
                        101, -2,
                        200, 2],
                      TimePeriod.Night,
                      3,
                      4))
