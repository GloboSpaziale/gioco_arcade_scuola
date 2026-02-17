import arcade
import torre
import barre_vita

class torre_grande_cattiva_class(torre.torre_class):
    
    def __init__(self):
        super().__init__()
        self.vita_torre=200
        self.altezza_creatura = 40

    def setup(self):
        self.torre = arcade.Sprite("./assets/torre_grande_cattiva.PNG")
        self.torre.center_x = 174
        self.torre.center_y = 530
        self.torre.scale = 0.45
        self.lista_torre.append(self.torre)
