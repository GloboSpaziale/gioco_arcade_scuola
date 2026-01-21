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
    
    def on_draw(self):
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0,0,self.larghezza,self.altezza)
        )

def main():
    gioco = Gioco()
    arcade.run()

if __name__ == "__main__":
    main()
