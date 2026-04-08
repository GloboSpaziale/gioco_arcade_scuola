import arcade

def draw_elisir_bar(elisir_attuale ,carica):
    HEALTHBAR_WIDTH = 250
    HEALTHBAR_HEIGHT = 30
    elisir = elisir_attuale
    massimo = 10
    x_attuale=50
    y_attuale=15

    ratio1 = max(0, min(1, elisir/massimo))
    ratio2 = max(0, min(1, carica/massimo))

    #Rettangolo nero (sfondo)
    arcade.draw_lbwh_rectangle_filled(
        x_attuale,
        y_attuale,
        HEALTHBAR_WIDTH,
        HEALTHBAR_HEIGHT,
        arcade.color.BLACK
    )

    #Rettangolo rosso (elisir in carica)
    arcade.draw_lbwh_rectangle_filled(
        x_attuale,
        y_attuale,
        HEALTHBAR_WIDTH * ratio2,
        HEALTHBAR_HEIGHT,
        arcade.color.RED
    )

    #Rettangolo viola (elisir attuale)
    arcade.draw_lbwh_rectangle_filled(
        x_attuale,
        y_attuale,
        HEALTHBAR_WIDTH * ratio1,
        HEALTHBAR_HEIGHT,
        arcade.color.PURPLE_PIZZAZZ
    )

    #bordo
    arcade.draw_lbwh_rectangle_outline(
        x_attuale,
        y_attuale,
        HEALTHBAR_WIDTH,
        HEALTHBAR_HEIGHT,
        arcade.color.BLACK,
        1
    )