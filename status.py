import pyxel
from world import *

class Status:
    def __init__(self):
        self.x0 = 10
        self.y0 = 10
        self.y_diff = 7
        self.time = 0.0
        self.speed = 0.0
        self.distance = 29.5 # dummy value for now
        self.best_time = 5.2 # dummy value for now

    def update(self):
        self.time = world.elapsed_time

    def show(self):
        x = self.x0
        y = self.y0
        pyxel.text(x, y, '    Time: {:5.1f}'.format(self.time), 1)
        y += self.y_diff
        pyxel.text(x, y, '   Speed: {:5.1f}'.format(self.speed), 1)
        y += self.y_diff
        pyxel.text(x, y, 'Distance: {:5.1f}'.format(self.distance), 1)
        y += self.y_diff * 2
        pyxel.text(x, y, 'Best Time: {:5.1f}'.format(self.best_time), 1)
