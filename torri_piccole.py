import arcade
import torre
import barre_vita

class torri_piccola_class(torre.torre_class):

    def __init__(self):
        super().__init__()
    
    def setup(self):
        self.torre = arcade.Sprite("./assets/torri_piccole.PNG")
        self.torre.center_x = 267
        self.torre.center_y = 150
        self.torre.scale = 0.40
        self.lista_torre.append(self.torre)
        self.torre = arcade.Sprite("./assets/torri_piccole.PNG")
        self.torre.center_x = 78
        self.torre.center_y = 150
        self.torre.scale = 0.40
        self.lista_torre.append(self.torre)