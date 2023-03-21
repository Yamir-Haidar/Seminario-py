from Matrix import Matrix
from utils.Numbers_Validations import solicit_numbers, solicit_numbers_for_fill_matrix,enter_position


m = Matrix(solicit_numbers("Ingrese la cantidad de filas", False), solicit_numbers("Ingrese la cantidad de columnas", False), solicit_numbers_for_fill_matrix())

for i in range(m.get_row()):
    print(f"{m.get_matrix_row(i)}")

print("\n")

print(m.divisor_of_3_for_column(enter_position(f"Ingrese la columna[1-{m.get_column()}] para determinar los numeros divisibles y mayores que 3: ", m.get_column())))
print("\n")

print("Coumnas cuya suma es mayor que 9: \n")
column = m.higer_9()

for i in range(len(column)):
    if column[i]:
        print(f"Sumatoria columna{i+1} mayor que 9\n")
    else:
        print(f"Sumatoria columna{i+1} menor o igual que 9\n")

print("\n")

pos = enter_position( f"Ingrese la fila[1-{m.get_row()}] para ordenarla de manera descendente: ", m.get_row() )
print("\n")
print(f"Desordenado: {m.get_matrix_row(pos)}")
print(f"Ordenado Descendente: {m.ordered_row(pos)}")



