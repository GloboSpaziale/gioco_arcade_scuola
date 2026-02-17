import arcade
import barre_vita

class torre_class(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.torre = None
        self.lista_torre = arcade.SpriteList()
        self.vita_torre = 100
        self.vita_attuale = 100
        self.altezza_creatura = 20


        self.setup()

    def setup(self):
        pass
    def on_draw(self):
        barre_vita.draw_health_bar(self.vita_torre,self.vita_attuale,self.torre.center_x,self.torre.center_y,self.altezza_creatura)
        self.lista_torre.draw()
        self.lista_torre.draw_hit_boxes(arcade.color.BAKER_MILLER_PINK)
    