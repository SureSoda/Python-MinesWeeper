import os
import random


def clear(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":\
                os.system ("cls")
MAP_LARGE_X = 10
MAP_LARGE_Y = 10
PLAYER = "_-o"
p_x = 0
p_y = 0
p_position = [p_x, p_y]
p_position[0] = p_x
p_position[1] = p_y
while True:
    #limite superior con contador  casillas
    
    print(" +",end="")
    for numero in range(MAP_LARGE_X):
        print("_{}_".format(numero),end="")
    print("+ ")
    
    #relleno hasta player en Y y X
    for y_coordenate in range(0, p_y, 1):
        print("{}|".format(y_coordenate), end="")
        for x_coordenate in range(0, MAP_LARGE_X, 1):
            print(" # ", end="")
        print("|")
    print("{}|".format(p_y), end="")
    
    #relleno hasta player en X
    for x_coordenate in range(0, p_x, 1):
        print(" # ", end="")
    print(PLAYER, end="")
    
    #relleno tras player en X
    for x_coordenate in range(p_x+1, MAP_LARGE_X, 1):
        print(" # ", end="")
    print("|")
    
    #relleno en Y y X deespues de player
    for y_coordenate in range(p_y+1, MAP_LARGE_Y, 1):
        print("{}|".format(y_coordenate), end="")
        for x_coordenate in range(0, MAP_LARGE_X, 1):
            print(" # ", end="")
        print("|")
    
    #borde inferior con numeracion
    print(" +", end="")
    for numero in range(MAP_LARGE_X):
        print("_{}_".format(numero), end="")
    print("+ ")
    
    #control de movimiento
    movement = input(" W\n"
                     "ASD").lower()
    
    clear()
    
    #aplicacion del movimiento en x o y
    
    if movement == "w":
        if p_y == 0:
            pass
        else:
            p_y += -1
    
    elif movement == "s":
        if p_y == MAP_LARGE_Y-1:
            pass
        else:
            p_y += +1
    
    elif movement == "a":
        if p_x == 0:
            pass
        else:
            p_x += -1
    
    elif movement == "d":
        if p_x == MAP_LARGE_X-1:
            pass
        else:
            p_x += +1
    