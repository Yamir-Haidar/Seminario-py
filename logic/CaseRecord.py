class CaseRecord:
    # Cargar el fichero y guardarlo en una lista

    def __init__(self, filename):
        self.records = []               # Registro de casos
        self.load_file(filename)        # Cargar el fichero al registro

    def load_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split(',')
                record = Person(data[0], data[1], data[2], data[3])
                self.records.append(record)


class Person:
    def __init__(self, id, commune, variant_type, vaccinated):
        self.id = id
        self.commune = commune
        self.variant_type = variant_type
        self.vaccinated = vaccinated

    def info(self):
        print(self.id, self.commune, self.variant_type, self.vaccinated)
