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


def predominate_omicron(record) -> dict:  # Comunas en las que predomina la variante omicron.
    result = {}
    for key, value in make_dictionary_communes_variant(record).items():
        if omicron_has_higher_frequency(value):
            result[key] = str(value).count("omicron")
    return result


def make_dictionary_communes_variant(record) -> dict:
    dictionary = {}
    for person in record.records:
        if not person.commune in dictionary.keys():
            dictionary[person.commune] = str(person.variant_type)
        else:
            dictionary[person.commune] += " - " + str(person.variant_type)
    return dictionary


def omicron_has_higher_frequency(string: str) -> bool:
    switch_case = {}
    for word in string.split(" - "):
        if word in switch_case:
            switch_case[word] += 1
        else:
            switch_case[word] = 1
    return max(switch_case, key=switch_case.get) == "omicron" and \
        list(switch_case.values()).count(switch_case["omicron"]) == 1
