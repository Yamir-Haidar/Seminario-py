import matplotlib.pyplot as graph


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


def print_dictionary(dictionary: dict) -> None:
    """
    Imprime por pantalla el diccionario introducido por parametros
    :param dictionary: dict
    :return: None
    """
    for key, value in dictionary.items():
        print(key, value)
