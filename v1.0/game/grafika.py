import pyglet

class Grafika(pyglet.sprite.Sprite):
    def __init__(self, *args, ime = "Nic", **kwargs):
        super().__init__(*args, **kwargs)

        self.texture = self.image.get_texture()
        #glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        self.ime = ime

    def collide_mouse(self, x, y):
        if(self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height):
            return(True)

    def draw(self):
        self.texture.blit(self.x, self.y)

    def povecaj(self, procent = 0):
        self.scale += (100 + procent)//100

    def resize(self, wid, hei):
        self.texture.width = wid
        self.texture.height = hei



class Kvadrat(Grafika):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, ime = "Kvadrat", **kwargs)

"""
class Krog(Grafika):
    def __init__(self):
        super().__init__()
"""
