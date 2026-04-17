import random
import nemico_globale

def spawna_cattivo(lista, elisir):
    da_spawnare=[]
    if elisir >= costo(lista):
        da_spawnare.extend(lista)
        return da_spawnare
    return None

def scelta_cattivo(mazzo):
    valore=11
    lista=[]
    while valore>8:
        lista=random.sample(mazzo,random.randint(1,4))
        valore=costo(lista)
    return lista

def costo(lista):
    somma=0
    for i in lista:
        somma+=i.costo
    return somma

def mazzo_cattivo ():
    mazzo=[]
    buono=nemico_globale.Enemy_general(random.randint(0,350),random.randint(325,600),"./assets/cattivo_BN.png",0.75,1,25,1.5,3,3)
    mazzo.append(buono)
    buono=nemico_globale.Enemy_general(random.randint(0,350),random.randint(325,600), "./assets/combattente_cattivo.png",0.75,0.5,28,1.25,5,3)
    mazzo.append(buono)
    buono=nemico_globale.Enemy_general(random.randint(0,350),random.randint(325,600), "./assets/danni_cattivo.png",0.65,1,28,1.25,5,3)
    mazzo.append(buono)
    buono=nemico_globale.Enemy_general(random.randint(0,350),random.randint(325,600), "./assets/goblin_cattivo.png",0.75,0.5,20,1.5,3,2)
    mazzo.append(buono)
    buono=nemico_globale.Enemy_general(random.randint(0,350),random.randint(325,600), "./assets/scheletro_cattivo.png",0.75,vita=11,danno=2.5)
    mazzo.append(buono)
    buono=nemico_globale.Enemy_general(random.randint(0,350),random.randint(325,600), "./assets/ragno_cattivo.png",0.75,0.6,22,1,3.5,2)
    mazzo.append(buono)
    buono=nemico_globale.Enemy_general(random.randint(0,350),random.randint(325,600), "./assets/tank_cattivo.png",0.75 ,0.1,65,2,10.5,6)
    mazzo.append(buono)
    buono=nemico_globale.Enemy_general(random.randint(0,350),random.randint(325,600), "./assets/veloce_cattivo.png",0.75,1.5,35,2,5.5,4)
    mazzo.append(buono)
    return mazzo