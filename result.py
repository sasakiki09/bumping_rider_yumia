import pyxel
from world import *
from stages import *

class Result:
    def __init__(self):
        self.center = world.screen_size.div(2.0)
        self.w = 8
        self.h = 8
        self.reset()
        self.font = pyxel.Font("fonts/VictoriaBold-8.bdf")
        self.color = 8
        self.bg_color = 7

    def reset(self):
        self.failed = False
        self.result_time = False

    def text(self, x, y, str):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1, 2]:
                if dx == 0 and dy == 0: continue
                pyxel.text(x + dx, y + dy, str, self.bg_color, self.font)
        pyxel.text(x, y, str, self.color, self.font)
        pyxel.text(x + 1, y, str, self.color, self.font)
        
    def show_failed(self):
        str = "FAILED"
        w = self.w * len(str)
        h = self.h
        x0 = self.center.x - w / 2
        y0 = self.center.y - h / 2
        self.text(x0, y0, str)
        str = "Press X to Retry"
        w = self.w * len(str)
        x0 = self.center.x - w / 2
        y0 += self.h * 2
        self.text(x0, y0, str)

    def show_goal(self):
        str = "Goal: {:5.2f} sec.".format(self.result_time)
        w = self.w * len(str)
        h = self.h
        x0 = self.center.x - w / 2
        y0 = self.center.y - h / 2
        self.text(x0, y0, str)
        str = "Press X for Next"
        if world.stage_index + 1 == len(stages):
            str = "Press X for 1st Stage"
        w = self.w * len(str)
        x0 = self.center.x - w / 2
        y0 += self.h * 2
        self.text(x0, y0, str)

    def show(self):
        if self.failed:
            self.show_failed()
        elif self.result_time:
            self.show_goal()

    def update(self, failed, result_time):
        self.failed = failed
        self.result_time = result_time
