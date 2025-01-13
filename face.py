import pyxel
from world import *

class Face:
    def __init__(self, image_index):
        self.image_index = image_index
        self.image = pyxel.images[image_index]
        self.image.load(0, 0, "images/face.png")
        self.width = 64
        self.height = 64
        self.scale = 2

    def show(self):
        margin = 5
        x = world.screen_size.x - self.width - self.width / self.scale - margin
        y = margin + self.height / self.scale
        pyxel.blt(x, y, self.image_index,
                  0, 0, self.width, self.height,
                  world.bg_index, 0, self.scale)
                  
