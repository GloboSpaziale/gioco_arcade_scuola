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
        for i in self.lista_torre :
            barre_vita.draw_health_bar(self.vita_torre,self.vita_attuale,i.center_x,i.center_y,self.altezza_creatura)
        self.lista_torre.draw()
        self.lista_torre.draw_hit_boxes(arcade.color.BAKER_MILLER_PINK)
    