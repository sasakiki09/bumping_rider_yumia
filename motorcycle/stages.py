import math
import random
from world import *
from savedata import *
from physics import *

class TimePeriod(Enum):
    Day = auto()
    Night = auto()

class Stage:
    def __init__(self, xy_array, time_period, music, seed):
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
random.seed(100)
xys = [-3, 0]
x = 0
y = 0
while x < 200:
    x_diff = random.uniform(0.0, 0.2)
    y_diff = random.uniform(-0.05, 0.05)
    x += x_diff
    y += y_diff
    xys.append(x)
    xys.append(y)
g_stages.append(Stage(xys,
                      TimePeriod.Day,
                      3,
                      0))

# stage 4
g_stages.append(Stage([ -3, 0,
                        10, 1,
                        20, 5,
                        20.1, -5,
                        25, -5,
                        25.1, 2,
                        30, 0,
                        100, 4,
                        101, -2,
                        200, 2],
                      TimePeriod.Night,
                      3,
                      4))
