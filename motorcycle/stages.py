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

    def update_best_time(self, time, play_record):
        self.last_time = time
        updated = (self.best_time == None or time < self.best_time)
        if updated:
            self.best_time = time
            index = g_world.stage_index
            g_savedata.set_time(index, self.best_time)
            g_savedata.set_record_a(index, play_record.str_a())
            g_savedata.set_record_b(index, play_record.str_b())
            g_savedata.save()

g_stages = []

# stage 1
g_stages.append(Stage([ -3, 0,
                      5, 1,
                      20, 0,
                      100, 1],
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

# stage 5
g_stages.append(Stage([-3, 0,
                       20, 4,
                       25, 0,
                       30, 4,
                       45, 5,
                       46, -5,
                       48, -5,
                       50, 4,
                       60, 0,
                       75, 5,
                       80, 2,
                       85, 4.5,
                       90, 2,
                       90.1, -5,
                       92, -5,
                       93, 2,
                       120, 2,
                       121, 0,
                       122, 2,
                       123, 4,
                       124, 4.5,
                       130, 1,
                       200, 5],
                      TimePeriod.Night,
                      2,
                      5,
                      0.2,
                      0.07))

