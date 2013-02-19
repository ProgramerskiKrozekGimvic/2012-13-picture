import pyglet
from game.screen import *
from pyglet.gl import *
from game import menugumb
from game import resources
from game import grafika
from game.seznami import *



@game_window.event
def on_draw():
    game_window.clear()


    ozadje.draw()
    '''
    pyglet.gl.glColor4f(0, 1, 1, 1)
    glLineWidth(25)
    pyglet.graphics.draw(2, GL_LINES, ('v2i', (500,0,0,500)))
    
    pyglet.gl.glColor4f(1, 0, 0, 0.1)
    glLineWidth(25)
    pyglet.graphics.draw(2, GL_LINES, ('v2i', (0,0,500,500)))
    '''
    menu_batch.draw()
    graphics_batch.draw()


@game_window.event
def on_mouse_press(x, y, button, modifiers):

    """
        1: levi
        4: desni
        2: klik kolescek
    """
    

    if(button == 1):
        global globalx, globaly
        globalx = x
        globaly = y
        """
        flag = True
        for i in menu_list[:]:

            if(i.collide_mouse(x, y) == True):
                flag = False

        if(flag):
            dodaj(x,y)
        """

    if(button == 4):
        #print(x, y, button)
        for i in graphics_list[:]:

            if(i.collide_mouse(x, y) == True):
                graphics_list.remove(i)

@game_window.event
def on_mouse_release(x, y, button, modifiers):
    print(globalx, globaly, x, y)
    if(button == 1):
        flag = True
        for i in menu_list[:]:

            if(i.collide_mouse(x, y) == True):
                flag = False

        if(flag):
            dodaj(x,y)

def update(dt):
    pass

def dodaj(x,y, scale=1):
    klik = grafika.Kvadrat(resources.klik_image, batch = graphics_batch)
    klik.x = x - resources.klik_image.width/2
    klik.y = y - resources.klik_image.height/2
    klik.scale = scale
    graphics_list.append(klik)


ozadje = pyglet.sprite.Sprite(resources.ozadje_image)




m1 = resources.m1_image
m2 = resources.m2_image

menu_list.append(menugumb.MenuGumb(img=m1, y=400, ime="1", batch=menu_batch))
#menu_list[-1].x = 100
#menu_list[-1].scale = 1
menu_list.append(menugumb.MenuGumb(img=m2, y=300, ime="2", batch=menu_batch))
menu_list.append(menugumb.MenuGumb(img=m1, y=200, ime="3", batch=menu_batch))
menu_list.append(menugumb.MenuGumb(img=m2, y=100, ime="4", batch=menu_batch))
menu_list.append(menugumb.MenuGumb(img=m1, y=0, ime="5", batch=menu_batch))




cursor = pyglet.window.ImageMouseCursor(resources.cursor_image, 18, 18)
game_window.set_mouse_cursor(cursor)

if(__name__ == '__main__'):
    #dodaj(200, 200, scale=5)
    pyglet.clock.schedule_interval(update, 1/240)
    pyglet.app.run()



