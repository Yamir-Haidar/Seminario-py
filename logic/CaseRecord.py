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


class CaseRecord:
    def __init__(self, filename):
        self.records = []               # Registro de personas con los casos
        self.__load_file__(filename)        # Cargar el fichero al registro

    def __load_file__(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(',')
                record = Person(data[0], data[1], data[2], data[3])
                self.records.append(record)

    def make_dictionary_communes_cases(self) -> dict:
        """
        Devuelve un diccionario con los nombres de las comunas como clave
        del diccionario y el total de casos de esa comuna como valor.
        :return: dict
        """
        dictionary = {}
        for person in self.records:
            if person.commune in dictionary:
                dictionary[person.commune] += 1
            else:
                dictionary[person.commune] = 1
        return dictionary

    def predominate_omicron(self) -> dict:  # Comunas en las que predomina la variante omicron.
        """
        Devuelve un diccionario con las comunas donde predomina el omicron
        como clave y la cantidad de casos de omicron como valor.
        :return: dict
        """
        result = {}
        for key, value in self.make_dictionary_communes_variant().items():
            if __omicron_has_higher_frequency__(value):
                result[key] = str(value).count("omicron")
        return result

    def make_dictionary_communes_variant(self) -> dict:
        """
        Devuelve un diccionario con las comunas como clave y los tipos de
        variantes presentes como valor
        :return: dict
        """
        dictionary = {}
        for person in self.records:
            if not person.commune in dictionary.keys():
                dictionary[person.commune] = str(person.variant_type)
            else:
                dictionary[person.commune] += " - " + str(person.variant_type)
        return dictionary


class Person:
    def __init__(self, id, commune, variant_type, vaccinated):
        self.id = id
        self.commune = commune
        self.variant_type = variant_type
        self.vaccinated = vaccinated
