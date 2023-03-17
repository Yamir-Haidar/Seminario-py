import matplotlib.pyplot as graph
from logic.CaseRecord import CaseRecord


def make_dictionary_communes_cases(record: CaseRecord) -> dict:
    """
    Devuelve un diccionario con los nombres de las comunas como clave
    del diccionario y el total de casos de esa comuna como valor.
    :param record: CaseRecord
    :return: dict
    """
    dictionary = {}
    for person in record.records:
        if person.commune in dictionary:
            dictionary[person.commune] += 1
        else:
            dictionary[person.commune] = 1
    return dictionary


def make_graph(dictionary: dict) -> None:
    """
    Muestra un grafico de barras horizontales mediante SciView tomando
    como valores de (x) los valores de las claves del diccionario(y).
    :param dictionary: dict
    :return: None
    """
    graph.figure(figsize=(10, 6))
    graph.barh(list(dictionary.keys()), list(dictionary.values()))
    graph.title("Casos de COVID por comuna")
    graph.xlabel("Casos")
    graph.ylabel("Comuna")
    graph.show()


def predominate_omicron(record: CaseRecord) -> dict:  # Comunas en las que predomina la variante omicron.
    """
    Devuelve un diccionario con las comunas donde predomina el omicron
    como clave y la cantidad de casos de omicron como valor
    :param record: CaseRecord
    :return: dict
    """
    result = {}
    for key, value in make_dictionary_communes_variant(record).items():
        if omicron_has_higher_frequency(value):
            result[key] = str(value).count("omicron")
    return result


def make_dictionary_communes_variant(record: CaseRecord) -> dict:
    """
    Devuelve un diccionario con las comunas como clave y los tipos de
    variantes presentes como valor
    :param record: CaseRecord
    :return: dict
    """
    dictionary = {}
    for person in record.records:
        if not person.commune in dictionary.keys():
            dictionary[person.commune] = str(person.variant_type)
        else:
            dictionary[person.commune] += " - " + str(person.variant_type)
    return dictionary


def omicron_has_higher_frequency(string: str) -> bool:
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


def print_dictionary(dictionary: dict) -> None:
    """
    Imprime por pantalla el diccionario introducido por parametros
    :param dictionary: dict
    :return: None
    """
    for key, value in dictionary.items():
        print(key, value)
