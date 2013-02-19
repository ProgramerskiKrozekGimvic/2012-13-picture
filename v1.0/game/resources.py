import pyglet

pyglet.resource.path = ["../resources"]
pyglet.resource.reindex()

m1_image = pyglet.resource.image("gumb1.png")
m2_image = pyglet.resource.image("gumb2.png")
ozadje_image = pyglet.resource.image("ozadje.png")
cursor_image = pyglet.resource.image("cursor.png")
klik_image = pyglet.resource.image("klik.png")
klik_image.anchor_x = klik_image.width/2
klik_image.anchor_y = klik_image.height/2
