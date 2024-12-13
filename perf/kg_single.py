from rdflib import Graph
import json
import time


kg = Graph()
kg.parse('/data3/ams560-f24/project/mimic-sparql/build_mimicsparql_kg/mimic_sparqlstar_kg.xml', format='xml', publicID='/')

print("kg loaded")

def clean_text(val):
    if type(val) == str:
        val = val.replace("\\", ' ')
    return val

count = 0

# sparql = "select ?admission_type ?diagnoses_short_title where { </subject_id/74032> </hadm_id> ?hadm_id. ?hadm_id </admission_type> ?admission_type. ?hadm_id </diagnoses> ?diagnoses. ?diagnoses </diagnoses_icd9_code> ?diagnoses_icd9_code. ?diagnoses_icd9_code </diagnoses_short_title> ?diagnoses_short_title. }"
# sparql = json.loads(line)['sql'].replace("xmlschema","XMLSchema")
sparql = "select ( count ( distinct ?subject_id ) as ?agg )  where { ?subject_id </hadm_id> ?hadm_id. ?hadm_id </diagnoses> ?diagnoses. ?diagnoses </diagnoses_icd9_code> </diagnoses_icd9_code/e8788>. }"

# sparql = "select ( count ( distinct ?subject_id ) as ?agg )  where { ?subject_id </hadm_id> ?hadm_id. ?hadm_id </language> \"hait\"^^<http://www.w3.org/2001/XMLSchema#string>. }"
sparql = clean_text(sparql)
print(count, sparql)

start_time = time.time()
sparql_res = kg.query(sparql)
duration = time.time()-start_time

for res in sparql_res:
    val = '|'
    temp = []
    for t in res:
        val += str(t.toPython()) + '|\t\t|'
        # print(val)
        temp.append(str(t.toPython()))
        print(temp)
    # print(val[:-1])

duration2 = time.time()-start_time

print(temp,duration*1000,duration2*1000)
# w.write(str(count)+','+str(temp)+","+str(duration*1000)+','+str(duration2*1000)+'\n')