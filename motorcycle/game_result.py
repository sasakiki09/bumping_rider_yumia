import pyxel
from world import *
from savedata import *
from color_palette import *
from input import Button
from stages import *

class GameResult:
    SpriteSize = Vec2(64, 128)
    ImageScale = 2.5

    class CharaStat:
        def __init__(self):
            self.base = 0
            self.tits = 0
            self.head = 0
            self.larm = 0

    def __init__(self, image_path):
        self.image = pyxel.Image(256, 256)
        self.image.load(0, 0, image_path)
        self._set_sprite_offsets()
        self.font = pyxel.Font("fonts/spleen-16x32.bdf")
        self.small_font = pyxel.Font("fonts/spleen-8x16.bdf")
        margin = 10
        x = margin
        y = g_world.screen_size.y - Button.ButtonSize[1] - margin
        self.button = Button(x, y, "B")
        self.reset()

    def _set_sprite_offsets(self):
        sw = self.SpriteSize.x
        sh = self.SpriteSize.y
        self.base_offsets = [Vec2(0, 0), Vec2(0, sh)]
        self.tits_offsets = [Vec2(sw, 0), Vec2(sw, sh)]
        self.head_offsets = [Vec2(sw * 2, 0), Vec2(sw * 2, sh)]
        self.larm_offsets = [Vec2(sw * 3, 0), Vec2(sw * 3, sh)]
        self.max_y = [123, 111]

    def reset(self):
        self.tic = 0
        self.chara_base_y = g_world.screen_size.y + self.max_y[0]
        self.chara_stat = self.CharaStat()
        self.text_base_y = g_world.screen_size.y
        self.placed_tic = False
        self.best_total = None

    def fg_color(self):
        return ColorPalette.ResultTextFg

    def bg_color(self):
        return ColorPalette.ResultTextBg

    def update(self):
        self.tic += 1
        self._update_text_position()
        self._update_chara_position()
        if self.text_base_y <= 0 and not self.placed_tic:
            self.placed_tic = self.tic
        if self.best_total == None:
            total = 0
            for stage in g_stages:
                total += stage.last_time
            self._update_best_total(total)

    def _update_best_total(self, total):
        self.best_total = g_savedata.time(Savedata.TagTotal)
        if not self.best_total:
            self.best_total = total
        else:
            self.best_total = min(self.best_total, total)
        g_savedata.set_time(Savedata.TagTotal, self.best_total)
        g_savedata.save()

    def _update_text_position(self):
        if self.text_base_y > 0 and not self.placed_tic:
            self.text_base_y -= g_world.screen_size.y / 15
        if self.placed_tic:
            phase = (self.tic - self.placed_tic) * math.pi / 15
            self.text_base_y = 10 * math.sin(phase)
        
    def _update_chara_position(self):
        if self.chara_base_y > 0 and not self.placed_tic:
            self.chara_base_y -= g_world.screen_size.y / (15 * self.ImageScale)
            self.chara_stat = self.CharaStat()
        if not self.placed_tic: return
        period = 30
        phase = (self.tic - self.placed_tic) % period
        max_h = g_world.screen_size.y - self.SpriteSize.y * self.ImageScale
        h = ((phase / period * 2 - 1)**2) * max_h
        if h < 5:
            self.chara_base_y = g_world.screen_size.y - 10
            self.chara_stat.base = 1
            self.chara_stat.tits = 1
            self.chara_stat.larm = 1
        else:
            self.chara_base_y = g_world.screen_size.y - h - 5
            self.chara_stat.base = 0
            if phase % 15 < 7:
                self.chara_stat.tits = 1
            else:
                self.chara_stat.tits = 0
            self.chara_stat.larm = 0
        if phase < period / 2:
            self.chara_stat.head = 1
        else:
            self.chara_stat.head = 0

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
        i_w = self.SpriteSize.x
        i_h = self.SpriteSize.y
        i_s = self.ImageScale
        cx = g_world.screen_size.x - i_w * i_s / 2
        i_h2 = self.max_y[self.chara_stat.base]
        cy = self.chara_base_y + (i_h - i_h2) * i_s - i_h * i_s / 2
        spr_loc = self.base_offsets[self.chara_stat.base]
        blt_center(cx, cy, self.image,
                  spr_loc.x, spr_loc.y,
                  i_w, i_h,
                  g_world.bg_index, 0, i_s)
        spr_loc = self.tits_offsets[self.chara_stat.tits]
        blt_center(cx, cy, self.image,
                  spr_loc.x, spr_loc.y,
                  i_w, i_h,
                  g_world.bg_index, 0, i_s)
        spr_loc = self.head_offsets[self.chara_stat.head]
        blt_center(cx, cy, self.image,
                  spr_loc.x, spr_loc.y,
                  i_w, i_h,
                  g_world.bg_index, 0, i_s)
        spr_loc = self.larm_offsets[self.chara_stat.larm]
        blt_center(cx, cy, self.image,
                  spr_loc.x, spr_loc.y,
                  i_w, i_h,
                  g_world.bg_index, 0, i_s)

    def show_text(self):
        x0 = 20
        y0 = 20 + self.text_base_y / 2
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

