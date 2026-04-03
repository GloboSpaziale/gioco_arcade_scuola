import arcade
import torre
import torre_grande_cattiva
import torre_grande
import nemico_globale
import buoni_globale
import carte
import barra_elisir

LARGHEZZA = 350
ALTEZZA = 600
class Gioco(arcade.Window):
    def __init__(self):
        super().__init__(LARGHEZZA, ALTEZZA, "circa clash")
        self.altezza = ALTEZZA
        self.larghezza = LARGHEZZA
        self.background = None

        self.lista_torri_buone = arcade.SpriteList()
        self.lista_torri_cattive  = arcade.SpriteList()

        self.enemy_list = arcade.SpriteList()
        self.buoni_list = arcade.SpriteList()

        self.conta=0

        self.mouse_x = None
        self.mouse_y = None

        self.buoni = arcade.SpriteList()
        self.cattivi = arcade.SpriteList()

        self.game_over = False
        self.vittoria = False

        self.lista_muri = arcade.SpriteList(use_spatial_hash=True)

        self.nemico = None
        self.buono = None

        self.elisir = 0
        self.carica_elisir = 0
        self.percentuele_elisir = 0

        self.setup()
        

    def setup(self):
        
        self.background = arcade.load_texture("./assets/sfondo.png")

        #aggiungo le torri
        self.lista_torri_cattive.append(torre.torre_class("./assets/torri_piccole_cattive.PNG",0.40,267,465))
        self.lista_torri_cattive.append(torre.torre_class("./assets/torri_piccole_cattive.PNG",0.40,78,465))
        self.torre_grande_cattiva = torre_grande_cattiva.torre_grande_cattiva_class()
        self.lista_torri_cattive.append(self.torre_grande_cattiva)
        self.cattivi.extend(self.lista_torri_cattive)
        self.lista_torri_buone.append(torre.torre_class("./assets/torri_piccole.PNG",0.40,267,150))
        self.lista_torri_buone.append(torre.torre_class("./assets/torri_piccole.PNG",0.40,78,150))
        self.torre_grande = torre_grande.torre_grande_class()
        self.lista_torri_buone.append(self.torre_grande)
        self.buoni.extend(self.lista_torri_buone)

        muro = arcade.SpriteSolidColor(155.6, 51, arcade.color.RED) 
        muro.center_x = 175
        muro.center_y = 300
        self.lista_muri.append(muro)

        muro = arcade.SpriteSolidColor(64, 51, arcade.color.RED) 
        muro.center_x = 32
        muro.center_y = 300
        self.lista_muri.append(muro)

        muro = arcade.SpriteSolidColor(64, 51, arcade.color.RED)
        muro.center_x = 318
        muro.center_y = 300
        self.lista_muri.append(muro)
        

    def on_draw(self):

        self.clear()
        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0,0,self.larghezza,self.altezza)
        )

        self.enemy_list.draw()
        for i in self.enemy_list:
            i.on_draw()

        self.buoni_list.draw()
        for i in self.buoni_list:
            i.on_draw()

        self.lista_torri_cattive.draw()
        for i in self.lista_torri_cattive:
            i.on_draw()

            self.lista_torri_buone.draw()
        for i in self.lista_torri_buone:
            i.on_draw()

        barra_elisir.draw_elisir_bar(self.elisir,self.percentuele_elisir)

        self.lista_torri_cattive.draw_hit_boxes(arcade.color.BAKER_MILLER_PINK)
        self.lista_torri_buone.draw_hit_boxes(arcade.color.BAKER_MILLER_PINK)
        self.enemy_list.draw_hit_boxes(arcade.color.AMAZON)
        self.buoni_list.draw_hit_boxes(arcade.color.RED_DEVIL)

        if self.game_over:
            arcade.draw_lbwh_rectangle_filled(0, 0, 
                                         LARGHEZZA, ALTEZZA, 
                                         (0, 0, 0, 100))
            
            arcade.draw_text("GAME OVER", 
                             LARGHEZZA/2, ALTEZZA/2,
                             arcade.color.WHITE, font_size=30, 
                             anchor_x="center")
            return  
        
        if self.vittoria:
            arcade.draw_lbwh_rectangle_filled(0, 0, 
                                        LARGHEZZA, ALTEZZA, 
                                        (0, 0, 0, 100))
            
            arcade.draw_text("VITTORIA", 
                             LARGHEZZA/2, ALTEZZA/2,
                             arcade.color.WHITE, font_size=30, 
                             anchor_x="center")
            return
        

    def on_update(self,delta_time):

        if self.game_over or self.vittoria:
            return
        
        for enemy in self.enemy_list:
            enemy.movimento_verso_buoni(self.buoni,self.lista_muri)
            enemy.update_timer(delta_time)

        for enemy in self.enemy_list:
            
            if enemy.puo_attaccare():
                
                # Controlla se sta toccando un bersaglio
                bersagli_colpiti = arcade.check_for_collision(enemy, enemy.current_target)
                
                if bersagli_colpiti:
                    # Se tocca qualcuno, infliggi danno al primo bersaglio trovato
                    
                    if hasattr(enemy.current_target, "vita_attuale"):
                        enemy.current_target.vita_attuale -= enemy.danno

        for buoni in self.buoni_list:
            buoni.movimento_verso_cattivi(self.cattivi,self.lista_muri)
            buoni.update_timer(delta_time)

        for buoni in self.buoni_list:
            
            if buoni.puo_attaccare():
                
                # Controlla se sta toccando un bersaglio
                bersagli_colpiti = arcade.check_for_collision(buoni, buoni.current_target)
                
                if bersagli_colpiti:
                    # Se tocca qualcuno, infliggi danno al primo bersaglio trovato
                    if hasattr(buoni.current_target, "vita_attuale"):
                        buoni.current_target.vita_attuale -= buoni.danno
        
        for buoni in self.buoni_list:
            if buoni.vita_attuale <= 0:
                buoni.remove_from_sprite_lists()
        
        for buoni in self.lista_torri_buone:
            if buoni.vita_attuale <= 0:
                buoni.remove_from_sprite_lists()
        
        for enemy in self.enemy_list:
            if enemy.vita_attuale <= 0:
                enemy.remove_from_sprite_lists()
        
        for enemy in self.lista_torri_cattive:
            if enemy.vita_attuale <= 0:
                enemy.remove_from_sprite_lists()
        
        self.elisir_update(delta_time)
        
        if self.torre_grande.vita_attuale <= 0:
            self.game_over = True

        if self.torre_grande_cattiva.vita_attuale <= 0:
            self.vittoria = True


    def elisir_update(self,deltatime):
        self.carica_elisir += deltatime
        if self.carica_elisir >= 2:
            if self.elisir <10:
                self.elisir += 1
            self.carica_elisir = 0
        if self.percentuele_elisir <10:
            self.percentuele_elisir += deltatime/2
        
        

    def on_mouse_press(self, x, y, button,modifiers):
        self.mouse_x = x
        self.mouse_y = y
        
        if ((button == arcade.MOUSE_BUTTON_LEFT) and (self.nemico != None)):
            if y < 326 :
                return
            self.nemico.center_x=x
            self.nemico.center_y=y
            self.enemy_list.append(self.nemico)
            self.cattivi.append(self.nemico)
            self.nemico = None
        elif ((button == arcade.MOUSE_BUTTON_RIGHT) and (self.buono != None)) and (self.elisir>= self.buono.costo):
            if y > 274 :
                return
            self.buono.center_x = x
            self.buono.center_y = y
            self.buoni_list.append(self.buono)
            self.buoni.append(self.buono)
            self.percentuele_elisir -= self.buono.costo
            self.elisir -= self.buono.costo
            self.buono = None
    

    def on_key_press(self, symbol, modifiers):

        if symbol == arcade.key.KEY_1:
            self.buono=buoni_globale.Buoni_general(self.mouse_x,self.mouse_y)
        elif symbol == arcade.key.KEY_2:
            self.nemico=nemico_globale.Enemy_general(self.mouse_x,self.mouse_y)
        

def main():
    gioco = Gioco()
    arcade.run()

if __name__ == "__main__":
    main()