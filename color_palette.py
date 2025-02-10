import pyxel
from PIL import Image

class ColorPalette:
    MaxColors = 200
    TitleBg = 0
    DaySky = 0
    NightSky = 0
    StatusBg = 0
    StatusFg = 0
    Star = 0
    DayMountain = 0
    NightMountain = 0
    DayCloud = 0
    NightCloud = 0
    Ground0 = 0
    Ground1 = 0
    
    def __init__(self, paths):
        self.initial_colors = pyxel.colors.to_list()
        colors = pyxel.colors.to_list()
        ColorPalette.TitleBg = len(colors)
        colors.append(0x4d65b4)
        ColorPalette.TitleTextFg = len(colors)
        colors.append(0xf68181)
        ColorPalette.TitleTextBg = len(colors)
        colors.append(0xc32454)
        ColorPalette.DaySky = len(colors)
        colors.append(0x4fefff)
        ColorPalette.NightSky = len(colors)
        colors.append(0x19194f)
        ColorPalette.StatusBg = len(colors)
        colors.append(0xa7fbff)
        ColorPalette.StatusFg = len(colors)
        colors.append(0xd25e7f)
        ColorPalette.Star = len(colors)
        colors.append(0xedf3ba)
        ColorPalette.DayMountain = len(colors)
        colors.append(0x42a581)
        ColorPalette.NightMountain = len(colors)
        colors.append(0x3e6758)
        ColorPalette.DayCloud = len(colors)
        colors.append(0xd3e3f2)
        ColorPalette.NightCloud = len(colors)
        colors.append(0x83909f)
        ColorPalette.Ground0 = len(colors)
        colors.append(0xc7b272)
        ColorPalette.Ground1 = len(colors)
        colors.append(0x8f7320)
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
