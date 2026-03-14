import arcade
import random
import math
import barre_vita

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

class Buoni_general(arcade.Sprite):
    def __init__(self, image_file, scale, velocita_buono, vita):
        
        super().__init__(image_file, scale)

        self.velocita_buono = velocita_buono
        self.vita = vita
        self.margin = -50
        self.edge = random.randint(0,3)
        self.vita_attuale =20
        self.altezza_creatura=20
        self.buoni_list = arcade.sprite_list()

        self.current_target = None

        if self.edge == 0:  # alto
            self.center_x = random.randint(self.margin, SCREEN_WIDTH - self.margin)
            self.center_y = SCREEN_HEIGHT - self.margin
        elif self.edge == 1:  # destra
            self.center_x = SCREEN_WIDTH - self.margin
            self.center_y = random.randint(self.margin, SCREEN_HEIGHT - self.margin)
        elif self.edge == 2:  # basso
            self.center_x = random.randint(self.margin, SCREEN_WIDTH - self.margin)
            self.center_y = self.margin
        elif self.edge == 3:  # sinistra
            self.center_x = self.margin
            self.center_y = random.randint(self.margin, SCREEN_HEIGHT - self.margin)

    def find_nearest_target(self):
        nearest = None
        nearest_distance = float("inf")

        for target in self.buoni_list:
            dist = arcade.get_distance_between_sprites(self.Buoni_general, target)

            if dist < nearest_distance:
                nearest_distance = dist
                nearest = target

        return nearest

    def movimento_verso_giocatore(self,):
        # se non ho target o il target non esiste più
        if self.current_target is None or self.current_target not in self.targets:
            self.current_target = self.find_nearest_target()

        # inseguo il target salvato
        if self.current_target:

            dx = self.current_target.center_x - self.Enemy_general.center_x
            dy = self.current_target.center_y - self.Enemy_general.center_y

            distance = math.sqrt(dx*dx + dy*dy)

            if distance > 0:
                dx /= distance
                dy /= distance

                self.Buoni_general.center_x += dx * self.velocita_buono
                self.Buoni_general.center_y += dy * self.velocita_buono

    def on_draw(self):
        for i in self.enemy_list :
            barre_vita.draw_health_bar(self.vita,self.vita_attuale,i.center_x,i.center_y,self.altezza_creatura)
        self.buoni_list.draw()
        self.buoni_list.draw_hit_boxes(arcade.color.BAKER_MILLER_PINK)