class Matrix:

    def __init__(self, row: int, column: int, numbers: list):
        self.row = row
        self.column = column
        self.matriz: list

        self.fill_matrix(numbers)

    def fill_matrix(self, numbers: list):
        """
        Crea la matriz con las dimensiones deseadas y la rellena con los numeros
        introducidos por el usuario
        """
        self.matriz = [[0 for _ in range(self.column)] for _ in range(self.row)]
        print(self.matriz)
        k = 0
        for i in range(self.row):
            for j in range(self.column):
                if k == len(numbers):
                    k = 0
                self.matriz[i][j] = numbers[k]
                k += 1

    def divisor_of_3_for_column(self, column: int) -> list:
        """
        Retorna una lista con los numeros que son divisibles y mayores que 3 de una columna dada;
        en caso de no existir ninguno la lista estara vacia
        """
        divisor_of_3 = []

        for i in range(self.row):

            if self.matriz[i][column] % 3 == 0 and self.matriz[i][column] > 3:
                divisor_of_3.append(self.matriz[i][column])

        return divisor_of_3

    def higer_9(self) -> list:

        """
         Retorna una lista que contiene true en caso de que la suma de los numeros de una columna sea mayor que 9
         False en caso contrario
         """

        column = []

        for j in range(self.column):

            sum = 0

            for i in range(self.row):
                sum += self.matriz[i][j]

            if sum > 9:
                column.append(True)
            else:
                column.append(False)

        return column

    def ordered_row(self, row: int) -> list:

        """
         Retorna una fila dada de la matriz ordenada descendentemente
         """

        lis:list = self.matriz[row]
        lis.sort(reverse=True)

        return lis

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def get_matrix_row(self, i: int):
        """
         Retorna una fila dada de la matriz
         """
        return self.matriz[i]
