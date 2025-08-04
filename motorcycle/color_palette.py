import pyxel
from PIL import Image

class ColorPalette:
    MaxColors = 200
    TitleBg = 0
    TitleTextFg = 0
    TitleTextBg = 0
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
    GroundSurface = 0
    GroundGoal = 0
    ResultBg = 0
    ResultTextBg = 0
    ResultTextFg = 0
    
    def __init__(self, paths_w_gray, paths):
        self.initial_colors = pyxel.colors.to_list()
        self.colors = []
        self.inv_colors = {}
        self.colors = pyxel.colors.to_list()
        ColorPalette.TitleBg       = self._add_color(0x4d65b4)
        ColorPalette.TitleTextFg   = self._add_color(0xf68181)
        ColorPalette.TitleTextBg   = self._add_color(0xc32454)
        ColorPalette.DaySky        = self._add_color(0x4fefff)
        ColorPalette.NightSky      = self._add_color(0x19194f)
        ColorPalette.StatusBg      = self._add_color(0xa7fbff)
        ColorPalette.StatusFg      = self._add_color(0xd25e7f)
        ColorPalette.Star          = self._add_color(0xedf3ba)
        ColorPalette.DayMountain   = self._add_color(0x42a581)
        ColorPalette.NightMountain = self._add_color(0x3e6758)
        ColorPalette.DayCloud      = self._add_color(0xd3e3f2)
        ColorPalette.NightCloud    = self._add_color(0x83909f)
        ColorPalette.Ground0       = self._add_color(0xc7b272)
        ColorPalette.Ground1       = self._add_color(0x8f7320)
        ColorPalette.GroundSurface = self._add_color(0xaaca64)
        ColorPalette.GroundGoal    = self._add_color(0xffffc0)
        ColorPalette.ResultBg      = self._add_color(0x95b2ff)
        ColorPalette.ResultTextBg  = self._add_color(0x8ff8e2)
        ColorPalette.ResultTextFg  = self._add_color(0x4d65b4)

        #################### working 2025.08.05
        self.colors.extend(self._from_images(paths_w_gray))
        self.colors.extend(self._from_images(paths))
        pyxel.colors.from_list(self.colors)

    def _add_color(self, color):
        index = len(self.colors)
        self.colors.append(color)
        self.inv_colors[color] = index
        return index

    def _make_gray(self, color):
        r = color >> 16
        g = (color & 0xff00) >> 8
        b = color & 0xff
        v = max(min(int((r + g + b) / 3), 255), 0)
        return v * 0x010101
    
    def _from_images(self, paths):
        cols = []
        for path in paths:
            image = Image.open(path)
            cols.extend(image.getcolors(maxcolors = self.MaxColors))
        cols = set(cols)
        if len(cols) > self.MaxColors: raise
        pal_cols = set()
        for col in cols:
            r, g, b, _ = col[1]
            pal_cols.add(r * 65536 + g * 256 + b)
        return pal_cols

    def _add_gray_colors(self, colors):
        gmap = []
        for col in colors:
            gray = _make_gray(col)
        #################### working 2025.08.04
