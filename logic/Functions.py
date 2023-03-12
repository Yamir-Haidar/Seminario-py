import matplotlib.pyplot as graph


def make_dictionary_communes_cases(record) -> dict:
    dictionary = {}
    for person in record.records:
        if person.commune in dictionary:
            dictionary[person.commune] += 1
        else:
            dictionary[person.commune] = 1
    return dictionary


def make_graph(dictionary):
    graph.figure(figsize=(10, 6))
    graph.barh(list(dictionary.keys()), list(dictionary.values()))
    graph.title("Casos de COVID por comuna")
    graph.xlabel("Casos")
    graph.ylabel("Comuna")
    graph.show()
