import arcade
import math
import nemico_globale

class buoni_class (arcade.Window):
    def __init__(self):
        pass
    def _event_key(self, ev):
        if ev == arcade.key.KEY_1:
            nemico_globale()
        return super()._event_key(ev)