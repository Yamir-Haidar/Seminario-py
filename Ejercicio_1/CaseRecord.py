from Person import Person


class CaseRecord:
    def __init__(self, filename):
        self.records = []                   # Registro de personas con los casos
        self.__load_file__(filename)         # Cargar el fichero al registro

    def __load_file__(self, filename: str) -> None:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                record = Person(data[0], data[1], data[2], data[3])
                self.records.append(record)

    @staticmethod
    def __omicron_has_higher_frequency__(variants: list) -> bool:
        """
        Devuelve True si el string "omicron" es el que sucede mas veces en
        el string introducido por parametros(En caso de empate con otro
        string en mayor numero de repeticiones, la funcion devolvera False).
        :param variants: list
        :return: bool
        """
        counter = {}
        for value in variants:
            if value in counter:
                counter[value] += 1
            else:
                counter[value] = 1

        # Encuentra el valor que se repite la mayor cantidad de veces y es el único que se repite esa cantidad de veces
        max_value = max(counter, key=counter.get)
        boolean = list(counter.values()).count(counter[max_value]) == 1 and max_value == "omicron"
        return boolean

    def make_dictionary_communes_cases(self) -> dict:
        """
        Devuelve un diccionario con los nombres de las comunas como clave
        del diccionario y el total de casos de esa comuna como valor.
        :return: dict
        """
        result = {}
        for person in self.records:
            if person.commune in result:
                result[person.commune] += 1
            else:
                result[person.commune] = 1
        return result

    def predominate_omicron(self) -> dict:  # Comunas en las que predomina la variante omicron.
        """
        Devuelve un diccionario con las comunas donde predomina el omicron
        como clave y la cantidad de casos de omicron como valor.
        :return: dict
        """
        result = {}
        for key, value in self.make_dictionary_communes_variant().items():
            if self.__omicron_has_higher_frequency__(value):
                result[key] = str(value).count("omicron")
        return result

    def make_dictionary_communes_variant(self, commune=None) -> dict:
        """
        Devuelve un diccionario con las comunas como clave y los tipos de
        variantes presentes como valor
        :return: dict
        """
        result = {}
        if commune is None:
            for person in self.records:
                if not person.commune in result.keys():
                    result[person.commune] = [person.variant_type]
                else:
                    result[person.commune].append(person.variant_type)
        else:
            for person in self.records:
                if person.commune == commune:
                    if person.commune in result.keys():
                        result[person.commune].append(person.variant_type)
                    else:
                        result[person.commune] = [person.variant_type]
        return result

    def percentage_variant(self, commune: str) -> dict:
        """
        Devuelve un diccionario con el nombre de la comuna y el porcentaje
        para cada variante presente en esta
        :param commune: str
        :return: dict
        """
        result = self.make_dictionary_communes_variant(commune)
        result_helper = {}
        # variants = str(result.values())
        for element in result.get(commune):
            if element in result_helper:
                result_helper["Variante " + element] += 1
            else:
                result_helper["Variante " + element] = 1
        for key, value in result_helper.items():
            result_helper[key] = str(round(value / len(result.get(commune)) * 100, 2)) + "%"
        result[commune] = result_helper
        return result

    def total_vaccinated(self) -> int:
        """
        Devuelve el numero de personas vacunadas
        :return: int
        """
        result = 0
        for person in self.records:
            if person.vaccinated == "si":
                result += 1
        return result
