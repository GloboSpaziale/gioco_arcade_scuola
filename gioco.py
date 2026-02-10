import arcade

LARGHEZZA = 350
ALTEZZA = 600
class Gioco(arcade.Window):
    def __init__(self):
        super().__init__(LARGHEZZA, ALTEZZA, "circa clash")
        self.altezza = ALTEZZA
        self.larghezza = LARGHEZZA
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture("./assets/sfondo.png")
        self.torre_piccola = None
        self.torre_grande = None
        self.lista_torre_piccola = arcade.SpriteList()
        self.lista_torre_grande = arcade.SpriteList()
        self.torre_piccola_cattiva = None
        self.torre_grande_cattiva = None
        self.lista_torre_piccola_cattiva = arcade.SpriteList()
        self.lista_torre_grande_cattiva = arcade.SpriteList()

        self.setup()
    def setup(self):
        def buoni():
            self.torre_piccola = arcade.Sprite("./assets/torri_piccole.PNG")
            self.torre_piccola.center_x = 267
            self.torre_piccola.center_y = 150
            self.torre_piccola.scale = 0.40
            self.lista_torre_piccola.append(self.torre_piccola)
            self.torre_piccola = arcade.Sprite("./assets/torri_piccole.PNG")
            self.torre_piccola.center_x = 78
            self.torre_piccola.center_y = 150
            self.torre_piccola.scale = 0.40
            self.lista_torre_piccola.append(self.torre_piccola)
            self.torre_grande = arcade.Sprite("./assets/torre_grande.png")
            self.torre_grande.center_x = 174
            self.torre_grande.center_y = 115
            self.torre_grande.scale = 0.45
            self.lista_torre_grande.append(self.torre_grande)
        def cattivi():
            self.torre_piccola_cattiva = arcade.Sprite("./assets/torri_piccole_cattive.png")
            self.torre_piccola_cattiva.center_x = 267
            self.torre_piccola_cattiva.center_y = 465
            self.torre_piccola_cattiva.scale = 0.40
            self.lista_torre_piccola_cattiva.append(self.torre_piccola_cattiva)
            self.torre_piccola_cattiva = arcade.Sprite("./assets/torri_piccole_cattive.png")
            self.torre_piccola_cattiva.center_x = 78
            self.torre_piccola_cattiva.center_y = 465
            self.torre_piccola_cattiva.scale = 0.40
            self.lista_torre_piccola_cattiva.append(self.torre_piccola_cattiva)
            self.torre_grande_cattiva = arcade.Sprite("./assets/torre_grande_cattiva.png")
            self.torre_grande_cattiva.center_x = 174
            self.torre_grande_cattiva.center_y = 530
            self.torre_grande_cattiva.scale = 0.45
            self.lista_torre_grande_cattiva.append(self.torre_grande_cattiva)
        buoni()
        cattivi()
    def on_draw(self):
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0,0,self.larghezza,self.altezza)
        )
        self.lista_torre_piccola.draw()
        self.lista_torre_grande.draw()
        self.lista_torre_piccola_cattiva.draw()
        self.lista_torre_grande_cattiva.draw()

    def on_update(self,deltatime):
        print("ciao")

def main():
    gioco = Gioco()
    arcade.run()

if __name__ == "__main__":
    main()
