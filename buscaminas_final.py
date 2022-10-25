import random
import re
import time
from string import ascii_lowercase


def setupgrid(gridsize, start, numberofmines):
    emptygrid = [['0' for i in range(gridsize)] for i in range(gridsize)]

    mines = getmines(emptygrid, start, numberofmines)

    for i, j in mines:
        emptygrid[i][j] = 'X'

    grid = getnumbers(emptygrid)

    return (grid, mines)


def showgrid(grid):
    gridsize = len(grid)

    horizontal = '   ' + (4 * gridsize * '-') + '-'

    # Imprimir las letras del mapa :)
    toplabel = '     '

    for i in ascii_lowercase[:gridsize]:
        toplabel = toplabel + i + '   '

    print(toplabel + '\n' + horizontal)

    # Imprime los numeros de la fila de la izquierda
    for idx, i in enumerate(grid):
        row = '{0:2} |'.format(idx + 1)

        for j in i:
            row = row + ' ' + j + ' |'

        print(row + '\n' + horizontal)

    print('')


def getrandomcell(grid):
    gridsize = len(grid)

    a = random.randint(0, gridsize - 1)
    b = random.randint(0, gridsize - 1)

    return (a, b)


def getneighbors(grid, rowno, colno):
    gridsize = len(grid)
    neighbors = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (rowno + i) < gridsize and -1 < (colno + j) < gridsize:
                neighbors.append((rowno + i, colno + j))

    return neighbors


def getmines(grid, start, numberofmines):
    mines = []
    neighbors = getneighbors(grid, *start)

    for i in range(numberofmines):
        cell = getrandomcell(grid)
        while cell == start or cell in mines or cell in neighbors:
            cell = getrandomcell(grid)
        mines.append(cell)

    return mines


def getnumbers(grid):
    for rowno, row in enumerate(grid):
        for colno, cell in enumerate(row):
            if cell != 'X':
                # Obtiene los valores de los vecinos 
                values = [grid[r][c] for r, c in getneighbors(grid,
                                                              rowno, colno)]

                # Cuenta cuántas son minas
                grid[rowno][colno] = str(values.count('X'))

    return grid


def showcells(grid, currgrid, rowno, colno):
    # Salir de la función si la celda ya se mostró
    if currgrid[rowno][colno] != ' ':
        return

    # Muestra celda actual 
    currgrid[rowno][colno] = grid[rowno][colno]

    # Obtener los numeros vecinos SI la celda esta vacia 
    if grid[rowno][colno] == '0':
        for r, c in getneighbors(grid, rowno, colno):
            # Repetir funcion para cada vecino que no tenga una bandera 
            if currgrid[r][c] != 'B':
                showcells(grid, currgrid, r, c)


def playagain():
    choice = input('Jugar de nuevo? (s/n): ')

    return choice.lower() == 's'


def parseinput(inputstring, gridsize, helpmessage):
    cell = ()
    flag = False
    message = "Celda Inalida. " + helpmessage

    pattern = r'([a-{}])([0-9]+)(b?)'.format(ascii_lowercase[gridsize - 1])
    validinput = re.match(pattern, inputstring)

    if inputstring == 'ayuda':
        message = helpmessage

    elif validinput:
        rowno = int(validinput.group(2)) - 1 # Coincidir  varios patrones distintos dentro de la misma cadena de destino
        colno = ascii_lowercase.index(validinput.group(1))
        flag = bool(validinput.group(3))

        if -1 < rowno < gridsize:
            cell = (rowno, colno)
            message = ''

    return {'Celda': cell, 'Bandera': flag, 'Mensaje': message}


def playgame():
    gridsize = 9
    numberofmines = 10

    currgrid = [[' ' for i in range(gridsize)] for i in range(gridsize)]

    grid = []
    flags = []
    starttime = 0

    helpmessage = ("Escriba la columnas seguido de la fila(ej: a5). "
                   "Para poner o remover una bandera, agregue b a la celda (ej: a5b).UwU")

    showgrid(currgrid)
    print(helpmessage + "Escriba 'ayuda'para volver a mostrar este mensaje de nuevo.\n")

    while True:
        minesleft = numberofmines - len(flags)
        prompt = input('Escriba la celda ({} minas restantes): '.format(minesleft))
        result = parseinput(prompt, gridsize, helpmessage + '\n')

        message = result['Mensaje']
        cell = result['Celda']

        if cell:
            print('\n\n')
            rowno, colno = cell
            currcell = currgrid[rowno][colno]
            flag = result['Bandera']

            if not grid:
                grid, mines = setupgrid(gridsize, cell, numberofmines)
            if not starttime:
                starttime = time.time()

            if flag:
                # Poner una bandera si la celda esta vacia
                if currcell == ' ':
                    currgrid[rowno][colno] = 'B'
                    flags.append(cell)
                # sacar la bandera si ya hay una
                elif currcell == 'B':
                    currgrid[rowno][colno] = ' '
                    flags.remove(cell)
                else:
                    message = 'No puedes poner una bandera ahi :/'

            # Si ya hay una bandera, mostrar mensaje
            elif cell in flags:
                message = 'Ya hay una bandera ahi'

            elif grid[rowno][colno] == 'X':
                print('Has perdido! :( \n')
                showgrid(grid)
                if playagain():
                    playgame()
                return

            elif currcell == ' ':
                showcells(grid, currgrid, rowno, colno)

            else:
                message = "Esa celda ya la puedes ver"

            if set(flags) == set(mines):
                minutes, seconds = divmod(int(time.time() - starttime), 60)
                print(
                    'Has ganado!. '
                    'Te tomo {} minutos y {} segundos en total.\n'.format(minutes,
                                                                      seconds))
                showgrid(grid)
                if playagain():
                    playgame()
                return

        showgrid(currgrid)
        print(message)
playgame()