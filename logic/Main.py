from logic.CaseRecord import CaseRecord
from logic.Functions import make_graph, make_dictionary_communes_cases, predominate_omicron, print_dictionary

case_record = CaseRecord("../casosCovid.txt")
cases_by_commune = make_dictionary_communes_cases(case_record)
print("Cantidad de casos por comuna:")
print_dictionary(cases_by_commune)
print("\n********************************************************\n")
make_graph(cases_by_commune)
communes_predominate_omicron = predominate_omicron(case_record)
print("Comunas donde predomina la variante omicron:")
print_dictionary(communes_predominate_omicron)
