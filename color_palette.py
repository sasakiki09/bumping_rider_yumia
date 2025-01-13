import pyxel

class ColorPalette:
    def __init__(self):
        self.initial_colors = pyxel.colors.to_list()
        colors = pyxel.colors.to_list()
        self.sky = len(colors)
        colors.append(0x4fefff)
        colors.extend(self.face_colors())
        pyxel.colors.from_list(colors)

    def face_colors(self):
        return [0xe8b796, 0xb86f50, 0xf6757a, 0x181425,
                0x5a6988, 0x3a4466, 0xc0cbdc, 0xa22633,
                0xb86f50, 0xf3e761, 0xffffff]
                  
