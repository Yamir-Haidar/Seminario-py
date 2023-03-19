from Person import Person


class CaseRecord:
    def __init__(self, filename):
        self.records = []                # Registro de personas con los casos
        self.__load_file__(filename)     # Cargar el fichero al registro

    def __load_file__(self, filename: str) -> None:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(',')
                record = Person(data[0], data[1], data[2], data[3])
                self.records.append(record)

    @staticmethod
    def __omicron_has_higher_frequency__(string: str) -> bool:
        """
        Devuelve True si el string "omicron" es el que sucede mas veces en
        el string introducido por parametros(En caso de empate con otro
        string en mayor numero de repeticiones, la funcion devolvera False).
        :param string: str
        :return: bool
        """
        switch_case = {}
        for word in string.split(" - "):
            if word in switch_case:
                switch_case[word] += 1
            else:
                switch_case[word] = 1
        return max(switch_case, key=switch_case.get) == "omicron" and \
            list(switch_case.values()).count(switch_case["omicron"]) == 1

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
        for person in self.records:
            if commune is None:
                if not person.commune in result.keys():
                    result[person.commune] = str(person.variant_type)
                else:
                    result[person.commune] += " - " + str(person.variant_type)
            else:
                if person.commune == commune:
                    if person.commune in result:
                        result[person.commune] += " - " + person.variant_type
                    else:
                        result[person.commune] = person.variant_type
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
        variants = str(result[commune]).split(" - ")
        for string in variants:
            if string in result_helper:
                result_helper["Variante " + string] += 1
            else:
                result_helper["Variante " + string] = 1
        for key, value in result_helper.items():
            result_helper[key] = str(round(value / len(variants) * 100, 2)) + "%"
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
