from logic.CaseRecord import CaseRecord
from logic.Functions import make_graph, make_dictionary_communes_cases, predominate_omicron, print_dictionary

# Creo la clase que contiene los registros
case_record = CaseRecord("../casosCovid.txt")

# Creo un diccionario que contiene los casos por comunas
cases_by_commune = make_dictionary_communes_cases(case_record)
print("Cantidad de casos por comuna:")

# Imprimo la informacion
print_dictionary(cases_by_commune)

# Imprimo el grafico de barras horizontales
make_graph(cases_by_commune)
print("\n********************************************************\n")

# Creo un diccionario que contiene las comunas donde predomina el omicron
communes_predominate_omicron = predominate_omicron(case_record)
print("Comunas donde predomina la variante omicron:")

# Imprimo la informacion
print_dictionary(communes_predominate_omicron)
