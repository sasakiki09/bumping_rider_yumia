import pyxel

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
        s.set_notes("RG3G3C4E4F4D4R")
        s.set_tones("PPPPPPPP")
        s.set_volumes("22222222")
        c1_1 = self.sound_index + 1
        s = pyxel.sounds[c1_1]
        s.set_notes("D2RA3G3E3G3B3B3")
        s.set_tones("PPPPPPPP")
        s.set_volumes("22222222")

        c2_0 = self.sound_index + 2
        s = pyxel.sounds[c2_0]
        s.set_notes("C4F3RRC4RF3R")
        s.set_tones("TTTTTTTT")
        s.set_volumes("22222222")
        c2_1 = self.sound_index + 3
        s = pyxel.sounds[c2_1]
        s.set_notes("C4F3RRC4RF3F3")
        s.set_tones("TTTTTTTT")
        s.set_volumes("22222222")

        c3_0 = self.sound_index + 4
        s = pyxel.sounds[c3_0]
        s.set_notes("RG2G2C3E3F3D3R")
        s.set_tones("SSSSSSS")
        s.set_volumes("22222222")
        c3_1 = self.sound_index + 5
        s = pyxel.sounds[c3_1]
        s.set_notes("D2RA2G2F2RA2A2")
        s.set_tones("SSSSSSS")
        s.set_volumes("22222222")
        
        pyxel.musics[0].set([],
                            [c1_0, c1_1],
                            [c2_0, c2_1],
                            [c3_0, c3_1])
