import pyxel
from world import *
from stages import *

class Result:
    def __init__(self):
        self.center = world.screen_size.div(2.0)
        self.w = 4
        self.h = 6
        self.reset()

    def reset(self):
        self.failed = False
        self.result_time = False

    def show_failed(self):
        w = self.w * 6
        h = self.h
        x0 = self.center.x - w / 2
        y0 = self.center.y - h / 2
        pyxel.text(x0, y0, "FAILED", 8)
        w = self.w * 17
        x0 = self.center.x - w / 2
        y0 += self.h * 2
        pyxel.text(x0, y0, "Press X to Retry", 8)

    def show_goal(self):
        w = self.w * 13
        h = self.h
        x0 = self.center.x - w / 2
        y0 = self.center.y - h / 2
        pyxel.text(x0, y0, "Goal {:5.2f}".format(self.result_time), 14)
        str = "Press X for Next"
        if world.stage_index + 1 == len(stages):
            str = "Press X for 1st Stage"
        w = self.w * len(str)
        x0 = self.center.x - w / 2
        y0 += self.h * 2
        pyxel.text(x0, y0, str, 14)

    def show(self):
        if self.failed:
            self.show_failed()
        elif self.result_time:
            self.show_goal()

    def update(self, failed, result_time):
        self.failed = failed
        self.result_time = result_time
