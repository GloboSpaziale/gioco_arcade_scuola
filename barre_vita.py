import arcade

def draw_health_bar(vita_massima : int,vita_attuale : int,x_creatura,y_creatura,altezza_creatura = 20, altezza_barra = 10, larghezza_barra = 60):
    HEALTHBAR_WIDTH = larghezza_barra
    HEALTHBAR_HEIGHT = altezza_barra
    vita = vita_attuale
    massimo = vita_massima
    x_attuale=x_creatura - HEALTHBAR_WIDTH/2
    y_attuale=y_creatura + altezza_creatura

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
