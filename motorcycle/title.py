import pyxel
import random
from world import *
from color_palette import *
from input import Button

class Title:
    ImageSize = Vec2(64, 128)
    ImageScale = 3
    
    def __init__(self, chara_path, text_path):
        self.chara_image = pyxel.Image(128, 128)
        self.chara_image.load(0, 0, chara_path)
        self.text_image = pyxel.Image(128, 128)
        self.text_image.load(0, 0, text_path)
        self.font = pyxel.Font("fonts/spleen-16x32.bdf")
        self.small_font = pyxel.Font("fonts/spleen-8x16.bdf")
        x = g_world.screen_size.x / 2 - Button.ButtonSize[0] / 2
        y = g_world.screen_size.y - Button.ButtonSize[1] - 10
        self.button = Button(x, y, "X")
        self.reset()

    def reset(self):
        self.tic = 0
        self.base_y = g_world.screen_size.y
        self.next_blink_tic = 20

    def fg_color(self):
        return ColorPalette.TitleTextFg

    def bg_color(self):
        return ColorPalette.TitleTextBg

    def pressed(self):
        return (pyxel.btn(pyxel.GAMEPAD1_BUTTON_X) or
                pyxel.btn(pyxel.KEY_X) or
                self.button.pressed())
    
    def update(self):
        self.tic += 1
        if self.base_y > 0:
            self.base_y -= g_world.screen_size.y / 15
        if self.base_y < 0:
            self.base_y = 0

    def sprite_location(self):
        if self.tic % self.next_blink_tic == 0:
            return Vec2(64, 0)
        elif self.tic % self.next_blink_tic == 1:
            self.next_blink_tic = random.randint(30, 90)
            return Vec2(64, 0)
        else:
            return Vec2(0, 0)            

    def text(self, x, y, str, font):
        pyxel.text(x, y - 1, str, self.bg_color(), font)
        pyxel.text(x - 1, y + 1, str, self.bg_color(), font)
        pyxel.text(x + 2, y + 1, str, self.bg_color(), font)
        pyxel.text(x + 1, y + 1, str, self.bg_color(), font)
        pyxel.text(x, y, str, self.fg_color(), font)

    def show_text_image(self):
        x = g_world.screen_size.x / 7
        y = g_world.screen_size.y / 4 + self.base_y
        pyxel.blt(x, y, self.text_image,
                  0, 0,
                  128, 128,
                  g_world.bg_index, 0, 2)

    def show_texts(self):
        x = g_world.screen_size.x / 8
        y = g_world.screen_size.y * 2 / 3 + self.base_y
        self.text(x, y, "Version {}".format(g_world.Version), self.small_font)
        x = g_world.screen_size.x / 9
        y = g_world.screen_size.y - 40 + self.base_y
        self.text(x, y, "Press X to start", self.small_font)

    def show_image(self):
        i_w = self.ImageSize.x
        i_h = self.ImageSize.y
        i_s = self.ImageScale
        cx = g_world.screen_size.x - i_w * i_s / 2
        cy = self.base_y + i_h * i_s / 2 - 10
        spr_loc = self.sprite_location()
        if spr_loc:
            blt_center(cx, cy, self.chara_image,
                      spr_loc.x, spr_loc.y,
                      i_w, i_h,
                      g_world.bg_index, 0, i_s)

    def show(self):
        pyxel.cls(ColorPalette.TitleBg)
        self.button.show()
        self.show_text_image()
        self.show_texts()
        self.show_image()
