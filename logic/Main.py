from logic.CaseRecord import CaseRecord
from logic.Functions import make_graph, make_dictionary_communes_cases, make_dictionary_communes_variant, \
    omicron_has_higher_frequency, predominate_omicron

case_record = CaseRecord("../casosCovid.txt")
cases_by_commune = make_dictionary_communes_cases(case_record)
print("Cantidad de casos por comuna:")
for key, value in cases_by_commune.items():
    print(key, value)
print("\n********************************************************\n")
make_graph(cases_by_commune)
communes_predominate_omicron = predominate_omicron(case_record)
print("Comunas donde predomina la variante omicron:")
for key, value in communes_predominate_omicron.items():
    print(key, value)
