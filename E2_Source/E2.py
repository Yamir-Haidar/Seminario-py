from E2_Source.Matrix import Matrix
from utils.Numbers_Validations import solicit_numbers, solicit_numbers_for_fill_matrix, enter_position

def e2():
    rows = solicit_numbers("Ingrese la cantidad de filas", False)
    cols = solicit_numbers("Ingrese la cantidad de columnas", False)
    matrix = Matrix(rows, cols, solicit_numbers_for_fill_matrix(rows*cols))

    for i in range(matrix.get_row()):
        print(f"{matrix.get_matrix_row(i)}")

    print("\n")

    print(matrix.divisor_of_3_for_column(enter_position(
        f"Ingrese la columna[1-{matrix.get_column()}] para determinar los números divisibles y mayores que 3: ",
        matrix.get_column()
    )))
    print("\n")

    print("Columnas cuya suma es mayor que 9: \n")
    column = matrix.higer_9()

    for i in column:
        if i:
            print(f"Sumatoria columna {i+1} mayor que 9\n")
        else:
            print(f"Sumatoria columna {i+1} menor o igual que 9\n")

    print("\n")

    pos = enter_position(
        f"Ingrese la fila[1-{matrix.get_row()}] para ordenarla de manera descendente: ", matrix.get_row())
    print("\n")
    print(f"Desordenado: {matrix.get_matrix_row(pos)}")
    print(f"Ordenado Descendente: {matrix.ordered_row(pos)}")
