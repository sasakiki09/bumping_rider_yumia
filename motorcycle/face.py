import pyxel
from game_constants import *
from world import *

class Face:
    Size = Vec2(85, 85)
    Scale = 2.5
    
    def __init__(self, image_index, path):
        self.image_index = image_index
        self.image = pyxel.images[image_index]
        self.image.load(0, 0, path)
        self.reset()

    def reset(self):
        self.index = FaceIndex.Empty

    def sprite_location(self):
        if self.index == FaceIndex.Empty:
            return False
        i_w = self.image.width
        h_count = i_w // self.Size.x
        x = int(self.index) % h_count
        y = int(self.index) // h_count
        return Vec2(x, y) * self.Size

    def update(self, index):
        self.index = index

    def show(self):
        cx = g_world.screen_size.x - self.Size.x * self.Scale / 2 + 15
        cy = self.Size.y * self.Scale / 2 + 10
        spr_loc = self.sprite_location()
        if spr_loc:
            blt_center(cx, cy, self.image_index,
                      spr_loc.x, spr_loc.y,
                      self.Size.x, self.Size.y,
                      g_world.bg_index, 0, self.Scale)
