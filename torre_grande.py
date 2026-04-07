import torre


class torre_grande_class(torre.torre_class):
    
    def __init__(self):
        super().__init__("./assets/torre_grande.PNG",0.45,174,115)
        self.vita_torre=200
        self.vita_attuale=200
        self.altezza_creatura = 40