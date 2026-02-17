import arcade
import barre_vita

class torre_class(arcade.Sprite):
    def __init__(self):
        
        self.torre = None
        self.lista_torre = arcade.SpriteList()
        self.vita_torre = 100
        self.vita_attuale = 100

        self.setup()

    def setup(self):
        pass
    def on_draw(self):
        self.lista_torre.draw()
        barre_vita.draw_health_bar(self.vita_torre,self.vita_attuale,self.torre.center_x,self.torre.center_y)
    