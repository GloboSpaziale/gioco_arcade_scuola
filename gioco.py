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
        self.nemico = nemico_globale.Enemy_general(20)
        self.buono = buoni_globale.Buoni_general(20)
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
        self.torre_big.on_draw()
        self.torre_small.on_draw()
        self.torre_big_hell.on_draw()
        self.torre_small_hell.on_draw()
        self.buoni_list.draw()
        self.buoni_list.draw()

    def on_update(self,delta_time):
        self.conta+=delta_time
        if self.conta>=2:
            self.enemy_list.append(self.nemico)
            self.buoni_list.append(self.buono)
            self.conta =0

        for enemy in self.enemy_list:
            nemico_globale.Enemy_general.movimento_verso_buoni(enemy=enemy, targets=self.buoni_list)
        for buoni in self.buoni_list:
            buoni_globale.Buoni_general.movimento_verso_cattivi(self.enemy_list)
        


def main():
    gioco = Gioco()
    arcade.run()

if __name__ == "__main__":
    main()
