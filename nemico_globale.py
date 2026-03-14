import arcade
import random
import math
import barre_vita
from buoni_globale import Buoni_general

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

class Enemy_general(arcade.Sprite):
    def __init__(self, image_file, scale, velocita_nemico, vita):
        
        super().__init__(image_file, scale)

        self.velocita_nemico = velocita_nemico
        self.vita = vita
        self.margin = -50
        self.edge = random.randint(0,3)
        self.vita_attuale =20
        self.altezza_creatura=20
        self.enemy_list = arcade.SpriteList()

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

    def assign_targets(self, targets):

        available_targets = list(Buoni_general.)

        for enemy in self.enemy_list:

            nearest = None
            nearest_distance = float("inf")

            for target in available_targets:
                dist = arcade.get_distance_between_sprites(enemy, target)

                if dist < nearest_distance:
                    nearest_distance = dist
                    nearest = target

            if nearest:
                enemy.current_target = nearest
                available_targets.remove(nearest)

    def movimento_verso_buoni(self,):
        # se non ho target o il target non esiste più
        if self.current_target is None or self.current_target not in self.targets:
            self.current_target = self.assign_targets()

        # inseguo il target salvato
        if self.current_target:

            dx = self.current_target.center_x - self.center_x
            dy = self.current_target.center_y - self.center_y

            distance = math.sqrt(dx*dx + dy*dy)

            if distance > 0:
                dx /= distance
                dy /= distance

                self.center_x += dx * self.velocita_nemico
                self.center_y += dy * self.velocita_nemico

    def on_draw(self):
        for i in self.enemy_list :
            barre_vita.draw_health_bar(self.vita,self.vita_attuale,i.center_x,i.center_y,self.altezza_creatura)
        self.enemy_list.draw()
        self.enemy_list.draw_hit_boxes(arcade.color.BAKER_MILLER_PINK)