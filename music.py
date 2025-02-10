import pyxel

# Note on converting from MSX MML:
# - Decrease 3 in "O" octave, and
# - Fix "T" tempo.
# MSX MML: https://www.minagi.jp/msxmmlreference/
# Pyxel MML: https://github.com/kitao/pyxel/blob/main/docs/faq-en.md#api-specification-and-usage

class Music:
    def __init__(self, sound_index):
        self.sound_index = sound_index
        self.channels = [1, 2, 3]
        self.set_music()

    def play(self):
        pyxel.playm(1, loop=True)

    def stop(self):
        for ch in self.channels:
            pyxel.stop(ch)

    def set_music(self):
        index = self.sound_index
        s = pyxel.sounds[index + 0]
        s.mml("T70V5L16" +
              "R16O2GGO3CEFDR16" +
              "DR16O2AGEGBB")
        s = pyxel.sounds[index + 1]
        s.mml("T70V5L16" +
              "O4CO3FR16R16O4CR16O3FR16" +
              "O4CO3FR16R16O4CR16O3FF")
        s = pyxel.sounds[index + 2]
        s.mml("T70V5L16" +
              "R16O1GGO2CEFDR16" +
              "DR16O1AGFR16AA")
        pyxel.musics[0].set([],
                            [index + 0],
                            [index + 1],
                            [index + 2])
        index += 3
        s = pyxel.sounds[index + 0]
        s.mml("T70V3L16@3" +
              "O0DO4AAO2CO0DO4AAO2C" +
              "O0DO4AAO2CO0DO4AAO2C")
        s = pyxel.sounds[index + 1]
        s.mml("T70V7L16@1" +
              "O1FABO2DDDO1EF" +
              "AAFAO2DEBO3C")
        s = pyxel.sounds[index + 2]
        s.mml("T70V7L16@2" +
              "O1CCO0AAFFAG" +
              "FFAR16O1DEAB")
        pyxel.musics[1].set([],
                            [index + 0],
                            [index + 1],
                            [index + 2])
              
