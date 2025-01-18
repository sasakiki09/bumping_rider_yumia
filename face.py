import pyxel
from world import *

class Face:
    Size = Vec2(64, 64)
    Scale = 2
    
    def __init__(self, image_index):
        self.image_index = image_index
        self.image = pyxel.images[image_index]
        self.image.load(0, 0, "images/faces.png")

    def show(self):
        margin = 5
        x = world.screen_size.x - self.Size.x - self.Size.x / self.Scale - margin
        y = margin + self.Size.y / self.Scale
        pyxel.blt(x, y, self.image_index,
                  0, 0, self.Size.x, self.Size.y,
                  world.bg_index, 0, self.Scale)
                  
