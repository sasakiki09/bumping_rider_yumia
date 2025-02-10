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
        pyxel.playm(0, loop=True)

    def stop(self):
        for ch in self.channels:
            pyxel.stop(ch)

    def set_music(self):
        c1_0 = self.sound_index
        s = pyxel.sounds[c1_0]
        s.mml("T60V5L16" +
              "R16O2GGO3CEFDR16" +
              "DR16O2AGEGBB")

        c2_0 = self.sound_index + 1
        s = pyxel.sounds[c2_0]
        s.mml("T60V5L16" +
              "O4CO3FR16R16O4CR16O3FR16" +
              "O4CO3FR16R16O4CR16O3FF")

        c3_0 = self.sound_index + 2
        s = pyxel.sounds[c3_0]
        s.mml("T60V5L16" +
              "R16O1GGO2CEFDR16" +
              "DR16O1AGFR16AA")
        
        pyxel.musics[0].set([],
                            [c1_0],
                            [c2_0],
                            [c3_0])
