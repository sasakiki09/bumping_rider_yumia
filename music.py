import pyxel

class Music:
    def __init__(self, sound_index):
        self.sound_index = sound_index
        self.set_music()

    def play(self):
        pyxel.playm(0, 20, loop=True)

    def stop(self):
        pyxel.stop(self.sound_index + 0)
        pyxel.stop(self.sound_index + 1)
        pyxel.stop(self.sound_index + 2)

    def set_music(self):
        si = self.sound_index
        pyxel.sounds[si].set_notes("RG3G3C4E4F4D4R")
        pyxel.sounds[si].set_tones("PPPPPPPP")
        pyxel.sounds[si].set_volumes("22222222")
        si += 1
        pyxel.sounds[si].set_notes("D2RA3G3E3G3B3B3")
        pyxel.sounds[si].set_tones("TTTTTTTT")
        pyxel.sounds[si].set_volumes("22222222")

        pyxel.musics[0].set([], [1,2], [], [])
