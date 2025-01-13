import math
from world import *
from physics import *

class Stage:
    def __init__(self, ground):
        self.ground = ground

ground = Ground(
    [Vec2(-3.0, 0.0),
     Vec2(5.0, 1.0),
     Vec2(20.0, 0.0),
     Vec2(100.0, 1.0)])

stages = []
stages.append(Stage(ground))
