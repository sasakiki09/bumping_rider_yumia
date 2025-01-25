import pyxel
from PIL import Image

class ColorPalette:
    MaxColors = 200
    
    def __init__(self, paths):
        self.initial_colors = pyxel.colors.to_list()
        colors = pyxel.colors.to_list()
        self.sky = len(colors)
        colors.append(0x4fefff)
        colors.extend(self.from_images(paths))
        pyxel.colors.from_list(colors)

    def from_images(self, paths):
        cols = []
        for path in paths:
            image = Image.open(path)
            cols.extend(image.getcolors(maxcolors = self.MaxColors))
        cols = set(cols)
        if len(cols) > self.MaxColors: raise
        pal_cols = []
        for col in cols:
            r, g, b, _ = col[1]
            pal_cols.append(r * 65536 + g * 256 + b)
        return pal_cols
