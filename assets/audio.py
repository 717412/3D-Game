
from ursina import Audio

class GameAudio:

    def __init__(self):
        self.sounds = {}

    def load_sound(self, name, filename):
        self.sounds[name] = Audio(
            filename,
            autoplay=False
        )

    def play(self, name):
        if name in self.sounds:
            self.sounds[name].play()

    def stop(self, name):
        if name in self.sounds:
            self.sounds[name].stop()
      
