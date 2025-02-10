import pyxel
from world import *
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
        y = world.screen_size.y - Button.ButtonSize[1] - margin
        self.button = Button(x, y, "B")
        self.reset()

    def reset(self):
        self.tic = 0
        self.base_y = world.screen_size.y
        self.placed_tic = False

    def fg_color(self):
        return ColorPalette.ResultTextFg

    def bg_color(self):
        return ColorPalette.ResultTextBg

    def update(self):
        self.tic += 1
        if self.base_y > 0 and not self.placed_tic:
            self.base_y -= world.screen_size.y / 15
        if self.base_y <= 0 and not self.placed_tic:
            self.placed_tic = self.tic
        if self.placed_tic:
            phase = (self.tic - self.placed_tic) * math.pi / 15
            self.base_y = 10 * math.sin(phase)

    def pressed(self):
        return (pyxel.btn(pyxel.GAMEPAD1_BUTTON_B) or
                pyxel.btn(pyxel.KEY_B) or
                self.button.pressed())

    def text(self, x, y, str):
        pyxel.text(x, y - 1, str, self.bg_color(), self.font)
        pyxel.text(x - 1, y + 1, str, self.bg_color(), self.font)
        pyxel.text(x + 2, y + 1, str, self.bg_color(), self.font)
        pyxel.text(x + 1, y + 1, str, self.bg_color(), self.font)
        pyxel.text(x, y, str, self.fg_color(), self.font)


    def show_image(self):
        i_w = self.ImageSize.x
        i_h = self.ImageSize.y
        i_s = self.ImageScale
        x = world.screen_size.x - i_w * i_s / 2 - i_w / 2 
        y = i_h * i_s / 2 - i_h / 2 - 10 + self.base_y
        spr_loc = self.ImageOffset
        pyxel.blt(x, y, self.image_index,
                  spr_loc.x, spr_loc.y,
                  i_w, i_h,
                  world.bg_index, 0, i_s)

    def show_text(self):
        x0 = 20
        y0 = 20 + self.base_y
        for index in range(len(stages)):
            time = stages[index].best_time
            self.text(x0, y0,
                      'Stage {}: {:7.2f}'.format(index + 1, time))
            y0 += 35

    def show(self):
        pyxel.cls(ColorPalette.ResultBg)
        self.show_image()
        self.show_text()
        self.button.show()

