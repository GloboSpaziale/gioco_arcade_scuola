import arcade
import torre_grande
import torre_grande_cattiva
import torri_piccole
import torri_piccole_cattive

LARGHEZZA = 350
ALTEZZA = 600
class Gioco(arcade.Window):
    def __init__(self):
        super().__init__(LARGHEZZA, ALTEZZA, "circa clash")
        self.altezza = ALTEZZA
        self.larghezza = LARGHEZZA
        arcade.set_background_color(arcade.color.BLACK)
        self.background = None

        self.setup()
    def setup(self):
        self.background = arcade.load_texture("./assets/sfondo.png")

        self.torre_big=torre_grande.torre_grande_class()
        self.torre_small=torri_piccole.torri_piccola_class()
        self.torre_big_hell=torre_grande_cattiva.torre_grande_cattiva_class()
        self.torre_small_hell=torri_piccole_cattive.torri_piccole_cattive_class()
        

    def on_draw(self):
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0,0,self.larghezza,self.altezza)
        )
        self.torre_big.on_draw()
        self.torre_small.on_draw()
        self.torre_big_hell.on_draw()
        self.torre_small_hell.on_draw()
        


    

    def on_update(self,deltatime):
        print("ciao")

def main():
    gioco = Gioco()
    arcade.run()

if __name__ == "__main__":
    main()
