import random
import arcade

def nuova_carta(appena_usata :arcade.Sprite,  lista_in_uso : arcade.SpriteList, lista_mazzo : arcade.SpriteList):
    lista_in_uso.remove(appena_usata)
    nuovo = appena_usata
    while ((nuovo == appena_usata) and (nuovo in lista_in_uso)):
        nuovo = random.choice(lista_mazzo)
    lista_in_uso.append(nuovo)
    return lista_in_uso

def prima_mano(lista_mazzo):
    return random.sample(lista_mazzo,4)
