grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 0]]

def imprimir_res(arr):
    """ funcion para imprimir sudoku correctamente """

    for y in range(len(arr)):
        output = ""
        for x in range(len(arr[y])):
            output += str(arr[y][x]) + " | "

        output = output[:-2]
        print(output)

def pos_possible(y,x,n):
    """ funcion que devuelve si el valor n es posible en la posición (y,x) """

    global grid

    for i in range(9):
        # comprobamos que el valor n no se encuentra en la fila y
        if grid[y][i] == n:
            return False
        # comprobamos que el valor n no se encuentra en la columna x
        if grid[i][x] == n:
            return False

    # comprobamos que el valor n no se encuentra en el grupo de 9 casillas
    y0 = (y // 3 ) * 3
    x0 = (x // 3 ) * 3

    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False 

    return True

def solve():
    """ funcion para resolver el sudoku """

    global grid

    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if pos_possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return 

    imprimir_res(grid)
    input("otra solución?")

if __name__ == "__main__":
    solve()
    print("No hay más soluciones")