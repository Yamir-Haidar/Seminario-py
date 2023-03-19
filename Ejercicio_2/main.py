
def Pedir_Numero(st) -> int:

    while True:

        try:

            num = int(input(f"{st}: "))
            print("\n")

            if num > 0:
                break
            else:
                print("El numero tiene que ser mayor que cero")

        except ValueError:
            print("Debe ingresar un numero entero!!!\n")

    return num

def Numeros_LLenado():

    lista = list()

    while True:

        print("Ingrese [-1] para salir!!\n")
        num = Pedir_Numero("Ingrese un numero:")
        if num == -1:




fila = Pedir_Numero("Ingrese la cantidad de filas")
columna = Pedir_Numero("Ingrese la cantidad de columnas")

listaNum = [1,2,8,4,2]
k = 0

matriz = [ [None for j in range(columna)] for i in range(fila)]

k = 0

for i in range(fila):
    for j in range(columna):

        matriz[i][j] = listaNum[k]

        k += 1

        if k == len(listaNum): k = 0


m: int
