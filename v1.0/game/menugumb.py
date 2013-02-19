import pyglet
from .seznami import *

class MenuGumb(pyglet.sprite.Sprite):
    def __init__(self, *args, ime = "Nic", **kwargs):
        super().__init__(*args, **kwargs)

        self.ime = ime

    def collide_mouse(self, x, y):
        if(self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height):
            print(self.ime)
            return(True)
            #self.povecaj(20)

    def povecaj(self, procent = 0):
        self.scale += (100 + procent)//100

"""
 self.pomanjsaj(20)

    def pomanjsaj(self, procent = 0):
        self.scale -= (100 - procent)//100
"""
