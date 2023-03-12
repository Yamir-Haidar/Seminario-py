from logic.CaseRecord import CaseRecord
from logic.Functions import make_graph, make_dictionary_communes_cases

case_record = CaseRecord("../casosCovid.txt")
cases_by_commune = make_dictionary_communes_cases(case_record)
make_graph(cases_by_commune)
