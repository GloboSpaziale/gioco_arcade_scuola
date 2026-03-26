import arcade
import torre
import barre_vita

class torre_grande_cattiva_class(torre.torre_class):
    
    def __init__(self):
        super().__init__("./assets/torre_grande_cattiva.PNG",0.45,174,530)
        self.vita_torre=200
        self.altezza_creatura = 40

