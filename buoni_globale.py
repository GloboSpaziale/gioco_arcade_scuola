import arcade
import math
import barre_vita

SCREEN_WIDTH = 350
SCREEN_HEIGHT = 600

class Buoni_general(arcade.Sprite):
    def __init__(self ,x ,y , velocita_buono =0.5, velocita_attacco = 1 ):
        
        super().__init__("./assets/torri_piccole.PNG", 0.2)

        self.velocita_buono = velocita_buono
        self.vita = 20
        self.vita_attuale = self.vita
        self.danno = 2

        self.frequenza_attacco = velocita_attacco
        self.timer_attacco = velocita_attacco
        
        self.altezza_creatura=20

        self.current_target = None

        self.center_x = x
        self.center_y = y

    def update_timer(self, delta_time):
        """Fa scorrere il tempo per il prossimo attacco"""
        if self.timer_attacco > 0:
            self.timer_attacco -= delta_time
        else:
            self.timer_attacco = self.frequenza_attacco

    def puo_attaccare(self):
        """Controlla se il timer è scaduto"""
        return self.timer_attacco <= 0

    def assign_targets(self, targets):

        available_targets = targets

        nearest = None
        nearest_distance = float("inf")

        for target in available_targets:
            dist = arcade.get_distance_between_sprites(self, target)

            if dist < nearest_distance:
                nearest_distance = dist
                nearest = target
        return nearest

    def movimento_verso_cattivi(self,targets):
        # se non ho target o il target non esiste più
        if self.current_target is None or self.current_target not in targets:
            self.current_target = self.assign_targets(targets)

        # inseguo il target salvato
        if self.current_target:

            dx = self.current_target.center_x - self.center_x
            dy = self.current_target.center_y - self.center_y

            distance = math.sqrt(dx*dx + dy*dy)

            if distance > 0:
                dx /= distance
                dy /= distance

                self.center_x += dx * self.velocita_buono
                self.center_y += dy * self.velocita_buono

    def on_draw(self):

        barre_vita.draw_health_bar(self.vita,self.vita_attuale,self.center_x,self.center_y,self.altezza_creatura)