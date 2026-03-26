import arcade
import barre_vita

class torre_class(arcade.Sprite):
    def __init__(self,path_or_texture, scala, x,y):
        super().__init__(path_or_texture, scala, x,y)
        self.torre = None
        self.vita_torre = 100
        self.vita_attuale = 100
        self.altezza_creatura = 20


        self.setup()

    def setup(self):
        pass
    def on_draw(self):
        barre_vita.draw_health_bar(self.vita_torre,self.vita_attuale,self.center_x,self.center_y,self.altezza_creatura,20,100)
    