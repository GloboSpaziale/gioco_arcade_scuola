import random

def nuova_carta(appena_usata,  lista_in_uso, lista_mazzo):
    nuova_lista=lista_in_uso
    nuovo = appena_usata
    nuova_lista.remove(nuovo)
    while nuovo in lista_in_uso:
        nuovo = random.choice(lista_mazzo)
    nuova_lista.append(nuovo)
    return nuova_lista

def prima_mano(lista_mazzo):
    return random.sample(lista_mazzo,4)

def nuovo_in_mano(nuovo,mano):
    for i in mano:
        if i==nuovo:
            return True
    
    return False

