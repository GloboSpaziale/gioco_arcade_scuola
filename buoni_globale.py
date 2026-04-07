import arcade
import math
import barre_vita

SCREEN_WIDTH = 350
SCREEN_HEIGHT = 600

class Buoni_general(arcade.Sprite):
    def __init__(self ,x ,y , texture="./assets/torri_piccole.PNG", scala = 0.2, velocita_buono =0.5, vita =20, velocita_attacco = 1, danno = 1, costo = 1):
        
        super().__init__(texture, scala)

        self.image_path = texture
        self.scala = scala

        self.velocita_buono = velocita_buono
        self.vita = vita
        self.vita_attuale = self.vita
        self.danno = danno

        self.costo=costo

        self.frequenza_attacco = velocita_attacco
        self.timer_attacco = velocita_attacco
        
        self.altezza_creatura = self.top - self.center_y

        self.current_target = None

        self.center_x = x
        self.center_y = y

    def clone(self):
        # Crea e restituisce una nuova istanza identica a questa
        return Buoni_general(self.center_x, self.center_y, self.image_path, self.scala,self.velocita_buono, self.vita,self.frequenza_attacco,self.danno, self.costo)

    def update_timer(self, delta_time):
        if self.timer_attacco > 0:
            self.timer_attacco -= delta_time
        else:
            self.timer_attacco = self.frequenza_attacco

    def puo_attaccare(self):
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
    
    def bordi(self):
    
        # Controllo Sinistra
        if self.left < 30:
            self.left = 30
        # Controllo Destra
        elif self.right > 320:
            self.right = 320

        # Controllo Basso
        if self.bottom < 0:
            self.bottom = 0
        # Controllo Alto
        elif self.top > 600 - (self.altezza_creatura+10):
            self.top = 600 - (self.altezza_creatura+10)

    def movimento_verso_cattivi(self,targets,lista_muri):
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
                if arcade.check_for_collision_with_list(self, lista_muri):
                    if self.left<=64:
                        self.center_x += 1
                    elif self.right>= 286:
                        self.center_x -= 1
                    elif (self.center_x<=175):
                        self.center_x -= 1
                    else:
                        self.center_x += 1
                    self.center_x -= dx * self.velocita_buono

                if not arcade.check_for_collision_with_list(self, lista_muri):
                    self.center_y += dy * self.velocita_buono
        self.bordi()

    def on_draw(self):

        barre_vita.draw_health_bar(self.vita,self.vita_attuale,self.center_x,self.center_y,self.altezza_creatura)