print("Bienvenido a Buscaminas")
opcion = input("[1]Como se juega \n"
        "[2]Partida normal\n"
        "[3]Modo peronalizado\n"
        "[4]Salir\n")

if opcion == "1":
    print("El juego consiste en despejar todas las casillas de una pantalla que no oculten una mina. Algunas casillas tienen un número, el cual" 
          "indica la cantidad de minas que hay en las casillas circundantes.")
if opcion == "2":
    print("Selecciona la dificulatad:\n")
    dificultad = input("[1]Facil\n"
                        "[2]Medio\n"
                        "[3]Dificil\n")
    
if opcion == "3":
    input("Ingrese las coordenada/s de la/s bomba/s:")
    
if opcion == "4":
    quit()