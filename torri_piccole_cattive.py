import arcade
import torre

class torri_piccole_cattive_class(torre.torre_class):

    def __init__(self):
        super().__init__()
    
    def setup(self):
        self.torre = arcade.Sprite("./assets/torri_piccole_cattive.PNG")
        self.torre.center_x = 267
        self.torre.center_y = 465
        self.torre.scale = 0.40
        self.lista_torre.append(self.torre)
        self.torre = arcade.Sprite("./assets/torri_piccole_cattive.PNG")
        self.torre.center_x = 78
        self.torre.center_y = 465
        self.torre.scale = 0.40
        self.lista_torre.append(self.torre)