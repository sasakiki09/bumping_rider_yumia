import pyxel
import PyxelUniversalFont as puf
from world import *

class Status:
    def __init__(self):
        self.x0 = 10
        self.y0 = 10
        self.y_diff = 9
        self.time = False
        self.speed = 0.0
        self.distance = 29.5
        self.best_time = False
        self.writer = puf.Writer("misaki_gothic2.ttf")

    def update(self, bike, ground):
        self.time = world.elapsed_time
        self.speed = bike.velocity.x
        self.distance = ground.goal_x() - bike.location.x

    def update_best_time(self):
        if not self.best_time:
            self.best_time = self.time
        self.best_time = min(self.best_time, self.time)

    def show(self):
        x = self.x0
        y = self.y0
        w = self.writer
        w.draw(x, y, 'STAGE: {:}'.format(world.stage_index + 1), 8, 1)
        y += self.y_diff * 2
        w.draw(x, y, '    Time: {:>7.2f}'.format(self.time), 8, 1)
        y += self.y_diff
        w.draw(x, y, '   Speed: {:>7.2f}'.format(self.speed), 8, 1)
        y += self.y_diff
        w.draw(x, y, 'Distance: {:>7.2f}'.format(self.distance), 8, 1)
        if self.best_time:
            y += self.y_diff * 2
            w.draw(x, y, 'Best Time: {:7.2f}'.format(self.best_time), 8, 1)
