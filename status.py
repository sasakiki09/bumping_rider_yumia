import pyxel
from world import *
from stages import *
from color_palette import ColorPalette

class Status:
    def __init__(self):
        self.x0 = 5
        self.y0 = 5
        self.y_diff = 8
        self.time = False
        self.speed = 0.0
        self.distance = 0.0

    def fg_color(self):
        return ColorPalette.StatusFg

    def bg_color(self):
        return ColorPalette.StatusBg

    def update(self, bike, ground):
        self.time = world.elapsed_time
        self.speed = bike.velocity.x
        self.distance = ground.goal_x() - bike.location.x

    def text(self, x, y, str):
        pyxel.text(x, y - 1, str, self.bg_color())
        pyxel.text(x - 1, y + 1, str, self.bg_color())
        pyxel.text(x + 2, y + 1, str, self.bg_color())
        pyxel.text(x + 1, y + 1, str, self.bg_color())
        pyxel.text(x, y, str, self.fg_color())

    def show(self):
        x = self.x0
        y = self.y0
        self.text(x, y, 'STAGE: {:}'.format(world.stage_index + 1))
        y += self.y_diff * 1.5
        self.text(x, y, '    Time: {:>7.2f}'.format(self.time))
        y += self.y_diff
        self.text(x, y, '   Speed: {:>7.2f}'.format(self.speed))
        y += self.y_diff
        self.text(x, y, 'Distance: {:>7.2f}'.format(self.distance))
        best_time = stages[world.stage_index].best_time
        if best_time:
            y += self.y_diff * 1.5
            self.text(x, y, 'Best Time: {:7.2f}'.format(best_time))
