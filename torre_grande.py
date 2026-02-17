import arcade
import torre

class torre_grande_class(torre.torre_class):
    
    def __init__(self):
        super().__init__()
        self.vita_torre=200

    def setup(self):
        self.torre = arcade.Sprite("./assets/torre_grande.PNG")
        self.torre.center_x = 174
        self.torre.center_y = 115
        self.torre.scale = 0.45
        self.lista_torre.append(self.torre)
