import arcade

def draw_health_bar(vita_massima : int,vita_attuale : int,x,y):
        HEALTHBAR_WIDTH =100
        HEALTHBAR_HEIGHT =25
        vita = vita_attuale
        massimo = vita_massima
        x_attuale=x - 45
        y_attuale=y

        ratio = max(0, min(1, vita/massimo))
        #Rettangolo rosso (sfondo)
        arcade.draw_lbwh_rectangle_filled(
            x_attuale,
            y_attuale,
            HEALTHBAR_WIDTH,
            HEALTHBAR_HEIGHT,
            arcade.color.RED
        )

        #Rettangolo verde (vita attuale)
        arcade.draw_lbwh_rectangle_filled(
            x_attuale,
            y_attuale,
            HEALTHBAR_WIDTH * ratio,
            HEALTHBAR_HEIGHT,
            arcade.color.GREEN
        )
