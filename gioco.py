import arcade

LARGHEZZA = 350
ALTEZZA = 600
class Gioco(arcade.Window):
    def __init__(self):
        super().__init__(LARGHEZZA, ALTEZZA, "Palline")
        arcade.set_background_color(arcade.color.BLACK)

def main():
    gioco = Gioco()
    arcade.run()

if __name__ == "__main__":
    main()
