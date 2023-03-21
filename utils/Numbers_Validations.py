def solicit_numbers(st: str, flag: bool) -> int:
    """""
    Valida que la entrada por consola sea un numero y que este sea mayor que cero

    Se pasa por parametros: 
    -Texto que queremos mostrar por consola
    -True: En caso de que se quiera permitir el [-1] / False: En caso contrario

    Retorna el numero ingresado

    """""
    while True:

        num = input(f"{st}: ")
        print("\n")

        if is_number(num):
            num = int(num)

            if num == -1 and flag:
                break

            elif num > 0:
                break

            else:
                print("El numero tiene que ser mayor que cero")

    return num


def solicit_numbers_for_fill_matrix() -> list:
    """""
    Retorna una lista con los numeros con los que se 
    va a rellenar la matriz
    """""

    numbers = []

    while True:

        print("Ingrese [-1] para salir")

        num: int = solicit_numbers("Ingrese un numero para rellenar la lista:", True)

        if num == -1:

            if len(numbers) == 0:

                print("Debe ingresar al menos un numero para rellenar la lista!!!\n")

            else:
                break

        else:

            numbers.append(num)

    return numbers


def is_number(number: str) -> bool:
    """
     Valida que la entrada por teclado sea un numero
    """

    try:

        n = int(number)

    except ValueError:

        print("Debe ingresar un numero!!!\n")
        return False

    return True


def enter_position(str: str, lim: int) -> int:
    """
      Valida que la entrada por teclado sea un numero y que el numero este en n rango de 1-X
      !Se usa para elegir una posicion de la matriz!
     """
    while True:

        position = input(f"{str}")

        if is_number(position):

            position = int(position)

            if position < 1 or position > lim:
                print(f"Debe seleccionar un numero entre 1 y {lim}!!!\n")

            else:
                break

    return position - 1
