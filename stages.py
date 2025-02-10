import math
from world import *
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
        
    def gen_ground(self, xy_array):
        l = len(xy_array)
        if l % 2 != 0: raise
        vec2_array = []
        for index in range(l // 2):
            x = xy_array[index * 2 + 0]
            y = xy_array[index * 2 + 1]
            vec2_array.append(Vec2(x, y))
        return Ground(vec2_array)

    def update_best_time(self, time):
        if self.best_time == None:
            self.best_time = time
        else:
            self.best_time = min(self.best_time, time)

stages = []

# stage 1
stages.append(Stage([ -3.0, 0.0,
                      5.0, 1.0,
                      20.0, 0.0,
                      100.0, 1.0],
                    TimePeriod.Day,
                    1,
                    0))

# stage 2
stages.append(Stage([ -3, 0,
                      10, 1,
                      20, 5,
                      20.1, 0,
                      50, 2,
                      100, 2],
                    TimePeriod.Night,
                    2,
                    1))
