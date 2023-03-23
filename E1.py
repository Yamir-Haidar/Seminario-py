from E1_Source.CaseRecord import CaseRecord
from utils.Functions import make_graph, print_dictionary, print_double_dictionary

# Creo la clase que contiene los registros
case_record = CaseRecord("E1_Source/casosCovid.txt")

# Creo un diccionario que contiene los casos por comunas
cases_by_commune = case_record.make_dictionary_communes_cases()
print("Cantidad de casos por comuna:")

# Imprimo la informacion
print_dictionary(cases_by_commune)
print("\n********************************************************\n")

# Imprimo el grafico de barras horizontales
make_graph(cases_by_commune)

print("Comunas donde predomina la variante omicron:")
print_dictionary(case_record.predominate_omicron())

print("\n********************************************************\n")

print("Porcentaje de casos en Villarrica:")
print_double_dictionary(case_record.percentage_variant("Villarrica"))

print("\n********************************************************\n")

print("Total de personas vacunadas:")
print(case_record.total_vaccinated())
