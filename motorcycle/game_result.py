import pyxel
from world import *
from savedata import *
from color_palette import *
from input import Button
from stages import *

class GameResult:
    ImageSize = Vec2(64, 128)
    ImageOffset = Vec2(128, 0)
    ImageScale = 3

    def __init__(self, image_index):
        self.image_index = image_index
        self.font = pyxel.Font("fonts/spleen-16x32.bdf")
        self.small_font = pyxel.Font("fonts/spleen-8x16.bdf")
        margin = 10
        x = margin
        y = g_world.screen_size.y - Button.ButtonSize[1] - margin
        self.button = Button(x, y, "B")
        self.reset()

    def reset(self):
        self.tic = 0
        self.base_y = g_world.screen_size.y
        self.placed_tic = False
        self.best_total = None

    def fg_color(self):
        return ColorPalette.ResultTextFg

    def bg_color(self):
        return ColorPalette.ResultTextBg

    def update(self):
        self.tic += 1
        if self.base_y > 0 and not self.placed_tic:
            self.base_y -= g_world.screen_size.y / 15
        if self.base_y <= 0 and not self.placed_tic:
            self.placed_tic = self.tic
        if self.placed_tic:
            phase = (self.tic - self.placed_tic) * math.pi / 15
            self.base_y = 10 * math.sin(phase)
        if self.best_total == None:
            total = 0
            for stage in g_stages:
                total += stage.last_time
            self.update_best_total(total)

    def update_best_total(self, total):
        self.best_total = g_savedata.time(Savedata.TagTotal)
        if not self.best_total:
            self.best_total = total
        else:
            self.best_total = min(self.best_total, total)
        g_savedata.set_time(Savedata.TagTotal, self.best_total)
        g_savedata.save()

    def pressed(self):
        return (pyxel.btn(pyxel.GAMEPAD1_BUTTON_B) or
                pyxel.btn(pyxel.KEY_B) or
                self.button.pressed())

    def text(self, x, y, str, font):
        pyxel.text(x, y - 1, str, self.bg_color(), font)
        pyxel.text(x - 1, y + 1, str, self.bg_color(), font)
        pyxel.text(x + 2, y + 1, str, self.bg_color(), font)
        pyxel.text(x + 1, y + 1, str, self.bg_color(), font)
        pyxel.text(x, y, str, self.fg_color(), font)

    def show_image(self):
        i_w = self.ImageSize.x
        i_h = self.ImageSize.y
        i_s = self.ImageScale
        x = g_world.screen_size.x - i_w * i_s / 2 - i_w / 2 
        y = i_h * i_s / 2 - i_h / 2 - 10 + self.base_y
        spr_loc = self.ImageOffset
        pyxel.blt(x, y, self.image_index,
                  spr_loc.x, spr_loc.y,
                  i_w, i_h,
                  g_world.bg_index, 0, i_s)

    def show_text(self):
        x0 = 20
        y0 = 20 + self.base_y / 2
        total_time = 0.0
        for index in range(len(g_stages)):
            time = g_stages[index].last_time
            total_time += time
            self.text(x0, y0,
                      'Stage {}: {:7.2f}'.format(index + 1, time),
                      self.font)
            y0 += 35
        y0 += 10
        self.text(x0, y0,
                  '  Total: {:7.2f}'.format(total_time),
                  self.font)
        y0 += 45
        if self.best_total:
            self.text(x0, y0,
                      'Best Total: {:7.2f}'.format(self.best_total),
                      self.font)
        x = g_world.screen_size.x / 8
        y = g_world.screen_size.y - 40
        self.text(x, y, "Press B", self.small_font)


    def show(self):
        pyxel.cls(ColorPalette.ResultBg)
        self.show_image()
        self.show_text()
        self.button.show()

