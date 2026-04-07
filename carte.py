import random

def nuova_carta(appena_usata,  lista_in_uso, lista_mazzo):
    nuova_lista=lista_in_uso
    nuova = appena_usata
    nuova_lista.remove(nuova)
    while carta_in_mano(nuova,lista_in_uso,appena_usata):
        nuova = lista_mazzo[random.randint(0,7)]
    nuova_lista.append(nuova)
    return nuova_lista

def prima_mano(lista_mazzo):
    return random.sample(lista_mazzo,4)

def nuovo_in_mano(nuovo,mano):
    if nuovo in mano:
        return True
    return False

def carta_in_mano(carta,lista_in_uso,appena_usata):
    if carta in lista_in_uso or carta==appena_usata:
        return True
    return False