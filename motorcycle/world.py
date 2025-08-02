import math
import time
from utilities import *

BikeWorldLen = 1.5 # [m]
BikeSpriteWidth = 96 # [pixel]
BikeSpriteHeight = 64 # [pixel]

class World:
    Version = "1.00"

    def __init__(self):
        self.gravity = Vec2(0.0, -9.8)
        self.scale = Vec2(BikeSpriteWidth / BikeWorldLen,
                          -BikeSpriteWidth / BikeWorldLen)
        self.screen_size = Vec2(480, 360)
        self.title = "Bumping Rider"
        self.bg_index = 0
        self.origin_world = Vec2(0.0, 0.0)
        self.origin_screen = Vec2(self.screen_size.x * 0.2,
                                  self.screen_size.y * 0.9)
        self.stage_index = 0

    def start(self):
        self.tic = 0
        self.start_time = time.time()
        self.last_time = self.start_time
        self.elapsed_time = 0.0
        self.delta_time = 0.0

    def update(self, world_origin):
        self.tic += 1
        now = time.time()
        self.delta_time = now - self.last_time
        self.elapsed_time = now - self.start_time
        self.last_time = now
        self.origin_world = world_origin

    def screen_xy(self, world_xy):
        w_diff = world_xy - self.origin_world
        s_diff = w_diff * self.scale
        return self.origin_screen + s_diff

    def world_xy(self, screen_xy):
        s_diff = screen_xy - self.origin_screen
        w_diff = s_diff / self.scale
        return self.origin_world + w_diff

g_world = World()
