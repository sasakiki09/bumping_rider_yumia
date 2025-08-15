import pyxel
import random
from world import *
from color_palette import *
from input import Button
from savedata import *
from stages import *

class Title:
    Margin = 10
    ImageSize = Vec2(64, 128)
    ImageScale = 3
    
    def __init__(self, chara_path, text_path):
        self.chara_image = pyxel.Image(128, 128)
        self.chara_image.load(0, 0, chara_path)
        self.text_image = pyxel.Image(128, 128)
        self.text_image.load(0, 0, text_path)
        self.font = pyxel.Font("fonts/spleen-16x32.bdf")
        self.small_font = pyxel.Font("fonts/spleen-8x16.bdf")
        x = g_world.screen_size.x / 3 - Button.ButtonSize[0]
        y = g_world.screen_size.y - self.Margin - Button.ButtonSize[1]
        self.start_button = Button(x, y, "X")
        x = g_world.screen_size.x * 5 / 9
        self.reset_button = Button(x, y, "Y", 13)
        self.a_button = None
        self.b_button = None
        self.reset()

    def reset(self):
        self.tic = 0
        self.base_y = g_world.screen_size.y
        self.next_blink_tic = 20
        self.show_reset_dialog = False

    def fg_color(self):
        return ColorPalette.TitleTextFg

    def bg_color(self):
        return ColorPalette.TitleTextBg

    def start_pressed(self):
        if self.show_reset_dialog: return False
        return (pyxel.btn(pyxel.GAMEPAD1_BUTTON_X) or
                pyxel.btn(pyxel.KEY_X) or
                self.start_button.pressed())

    def reset_pressed(self):
        if self.show_reset_dialog: return False
        return (pyxel.btn(pyxel.GAMEPAD1_BUTTON_Y) or
                pyxel.btn(pyxel.KEY_Y) or
                self.reset_button.pressed())
    
    def update(self):
        self.tic += 1
        if self.base_y > 0:
            self.base_y -= g_world.screen_size.y / 15
        if self.base_y < 0:
            self.base_y = 0
        if self.reset_pressed():
            self.show_reset_dialog = True
        if self.show_reset_dialog and self.a_button:
            a_pressed = (pyxel.btn(pyxel.GAMEPAD1_BUTTON_A) or
                         pyxel.btn(pyxel.KEY_A) or
                         self.a_button.pressed())
            b_pressed = (pyxel.btn(pyxel.GAMEPAD1_BUTTON_B) or
                         pyxel.btn(pyxel.KEY_B) or
                         self.b_button.pressed())
            if a_pressed:
                g_savedata.clear()
                g_savedata.save()
                for stage in g_stages:
                    stage.best_time = None
            if a_pressed or b_pressed:
                self.show_reset_dialog = False

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
        x = g_world.screen_size.x / 3 + self.Margin
        y = g_world.screen_size.y - 40 + self.base_y
        self.text(x, y, "Start", self.small_font)
        x = g_world.screen_size.x * 5 / 9 + Button.ButtonSize[0] + self.Margin
        pyxel.text(x, y, "Reset Best Time", self.fg_color(), self.small_font)

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

    def _show_reset_dialog(self):
        margin = self.Margin
        w = g_world.screen_size.x
        h = g_world.screen_size.y
        dw = w * 2 / 3
        dh = h / 2
        dx0 = w / 6
        dy0 = h / 4
        pyxel.rect(dx0, dy0, dw, dh, 12)
        x = w / 6 + margin * 2
        y = h / 4 + margin
        self.text(x, y, "Resetting Best Time. Are you sure?",  self.small_font)
        y = dy0 + dh * 3 / 4
        if not self.a_button:
            self.a_button = Button(dx0 + margin * 2, y, "A")
            self.b_button = Button(dx0 + dw / 2 + margin, y, "B")
        self.a_button.show()
        self.b_button.show()
        y += Button.ButtonSize[1] / 2 - Button.TextSize[1] / 2
        self.text(dx0 + Button.ButtonSize[0] + margin * 3, y, "Yes", self.small_font)
        self.text(dx0 + dw / 2 + Button.ButtonSize[0] + margin * 2, y, "No", self.small_font)

    def show(self):
        pyxel.cls(ColorPalette.TitleBg)
        self.show_text_image()
        self.show_image()
        self.start_button.show()
        self.reset_button.show()
        self.show_texts()
        if self.show_reset_dialog:
            self._show_reset_dialog()
