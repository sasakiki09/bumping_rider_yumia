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

    def play(self, index):
        pyxel.playm(index, loop=True)

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
        s.mml("T70V3L16@0" +
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
        index += 3
        s = pyxel.sounds[index + 0]
        s.mml("T70V6L16@2" +
              "O0CO1CO0FO1FCO2CO0AO1A" +
              "CCFFO2CCO1AA" +
              "O0CO1CO0FO1FCO2CO0AO1A" +
              "CCFFO2CCO1AA")
        s = pyxel.sounds[index + 1]
        s.mml("T70V6L16@1" +
              "O1AAO2CDGAO1AA" +
              "O2CDAO3CO1AO2CO3CD" +
              "R16O1GGAO2CFGO1A" +
              "AO2DFAO3DCO2AF")
        s = pyxel.sounds[index + 2]
        s.mml("T70V3L16@0" +
              "O1FFABO2EFO1FR16" +
              "AAO2FGO1FO2AAB" +
              "R16O1EEGAO2DER16" +
              "O1FO2CDFBAGD")
        pyxel.musics[2].set([],
                            [index + 0],
                            [index + 1],
                            [index + 2])
        index += 3
        s = pyxel.sounds[index + 0]
        s.mml("T70V6L16" +
              "O1CDEFABAB" +
              "EFABAGO2CO1B" +
              "O2DCFDO1BADC")
        s = pyxel.sounds[index + 1]
        s.mml("T70V6L16" +
              "O0ABO1DDGAGG" +
              "DDGGFEAG" +
              "BAO2DCO1AGCO0A")
        s = pyxel.sounds[index + 2]
        s.mml("T70V6L16" +
              "O2DDR16EFFFF" +
              "R16CCDFDCC" +
              "R16O1AAR16O2DFFR16")
        pyxel.musics[3].set([],
                            [index + 0],
                            [index + 1],
                            [index + 2])
        index += 3
        s = pyxel.sounds[index + 0]
        s.mml("T70V6L16" +
              "O1CEGO2CO1CEGO2C" +
              "O1CEGO2CO1CEGO2C" +
              "O1CEGO2CO1CEGO2C" +
              "O1CEGO2CO1CEGO2C")
        s = pyxel.sounds[index + 1]
        s.mml("T70V7L16@1" +
              "O3CCR16EER16GG" +
              "CCR16EER16GG" +
              "CCR16EEGGR16" +
              "CCCEEGGE")
        s = pyxel.sounds[index + 2]
        s.mml("T70V7L16@2" +
              "O3AAR16O4DDR16R16E" +
              "R16O3AR16O4DDR16R16E" +
              "R16O3AR16O4DDER16R16" +
              "R16O3AAO4DDER16D")
        pyxel.musics[4].set([],
                            [index + 0],
                            [index + 1],
                            [index + 2])
