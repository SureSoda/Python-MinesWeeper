import readchar
import os
import random

POS_X = 0
POS_Y = 1
ANCHO = 10
LARGO = 10
NUMERO_OBJETOS_MAPA = 11

mi_posicion = [3,1]
objetos_mapa = []

#Generador de bombas

while len(objetos_mapa) < NUMERO_OBJETOS_MAPA:
    nueva_posicion = [random.randint(0,ANCHO),random.randint(0,LARGO)]
    
    if nueva_posicion not in objetos_mapa and nueva_posicion != mi_posicion:
        objetos_mapa.append(nueva_posicion)
    
print(objetos_mapa)





while True: #Repeticon del mapa
#Diseño del mapa
    print("+" + "-" * ANCHO * 3 +"+") #Lo que aparece(la parte de arriba) antes del mapa

    for cordenada_y in range(LARGO): #Recorre el rango de la variable "LARGO" y a casa iteracion toma ese valor
        print("|",end="")
        for cordenada_x in range(ANCHO):  
            if mi_posicion[POS_X] == cordenada_x and mi_posicion[POS_Y] == cordenada_y: #Jugador
                print("@")
            else:
                print("  ",end="") # Para que el mapa no se rompa
        print("|")

    print("+" + "-" * ANCHO * 3 +"+")

    #Diseño de movimiento

    direccion = readchar.readchar().decode()
    print(direccion)

    if direccion == "w":
        mi_posicion[POS_Y]-= 1
    elif mi_posicion =="s":
        mi_posicion[POS_Y]+= 1
    elif mi_posicion =="a":
        mi_posicion[POS_X]-= 1
    elif mi_posicion =="d":
        mi_posicion[POS_X]+= 1
    

    
    
    
    os.system("cls")

    