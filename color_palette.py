import pyxel

class ColorPalette:
    def __init__(self):
        self.initial_colors = pyxel.colors.to_list()
        colors = pyxel.colors.to_list()
        self.sky = len(colors)
        colors.append(0x4fefff)
        pyxel.colors.from_list(colors)
        
