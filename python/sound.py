import pyxel

class Sound:
    def __init__(self, sound_index):
        self.channel = 0
        self.sound_index = sound_index
        s = pyxel.sounds[self.sound_index]
        s.speed = 2
        s.set_tones("P")
        s.set_effects("F")
        s.set_volumes("7")

    def note_str(self, ratio):
        base_ss = [
            "C",
            "C#",
            "D",
            "D#",
            "E",
            "F",
            "F#",
            "G",
            "G#",
            "A",
            "A#",
            "B"]
        base_len = len(base_ss)
        ratio = min(max(ratio, 0.0), 0.99)
        oct = int(ratio * 5)
        ratio_ = (ratio * 5) % 1.0
        key_index = int(ratio_ * base_len)
        key_s = base_ss[key_index]
        return key_s + str(oct)

    def update(self, ratio):
        if ratio:
            s = pyxel.sounds[self.sound_index]
            s.set_notes(self.note_str(ratio) + "R")
            pyxel.play(self.channel, 0, loop=True)
        else:
            pyxel.stop(self.channel)
