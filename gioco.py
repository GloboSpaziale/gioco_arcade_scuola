import arcade
import torre_grande
import torre_grande_cattiva
import torri_piccole
import torri_piccole_cattive
import nemico_globale
import buoni_globale

LARGHEZZA = 350
ALTEZZA = 600
class Gioco(arcade.Window):
    def __init__(self):
        super().__init__(LARGHEZZA, ALTEZZA, "circa clash")
        self.altezza = ALTEZZA
        self.larghezza = LARGHEZZA
        arcade.set_background_color(arcade.color.BLACK)
        self.background = None
        self.enemy_list = arcade.SpriteList()
        self.buoni_list = arcade.SpriteList()
        self.conta=0
        # self.nemico = nemico_globale.Enemy_general()
        # self.buono = buoni_globale.Buoni_general()
        self.setup()
        
    def setup(self):
        self.background = arcade.load_texture("./assets/sfondo.png")

        self.torre_big=torre_grande.torre_grande_class()
        self.torre_small=torri_piccole.torri_piccola_class()
        self.torre_big_hell=torre_grande_cattiva.torre_grande_cattiva_class()
        self.torre_small_hell=torri_piccole_cattive.torri_piccole_cattive_class()
        

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0,0,self.larghezza,self.altezza)
        )
        
        self.torre_small.on_draw()
        self.torre_small_hell.on_draw()
        self.torre_big_hell.on_draw()
        self.torre_big.on_draw()
        self.enemy_list.draw()
        self.enemy_list.draw_hit_boxes(arcade.color.AMAZON)
        self.buoni_list.draw()
        self.buoni_list.draw_hit_boxes(arcade.color.RED_DEVIL)

    def on_update(self,delta_time):
        self.conta+=delta_time
        if self.conta>2:
            for i in range (1,10):
                nemico = nemico_globale.Enemy_general()
                buono = buoni_globale.Buoni_general()
                self.enemy_list.append(nemico)
                self.buoni_list.append(buono)
                self.conta =0
        
        for enemy in self.enemy_list:
            enemy.movimento_verso_buoni(self.buoni_list)
            enemy.on_draw()
            # self.enemy_list.draw_hit_boxes(arcade.color.AMAZON)
        for buoni in self.buoni_list:
            buoni.on_draw()
            buoni.movimento_verso_cattivi(self.enemy_list)
            # self.buoni_list.draw_hit_boxes(arcade.color.RED_DEVIL)
    
        
        


def main():
    gioco = Gioco()
    arcade.run()

if __name__ == "__main__":
    main()
