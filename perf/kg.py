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

with open('/data3/ams560-f24/project/mimic-sparql/dataset/mimic_sparqlstar/natural/train.json') as f, open('results.csv','w') as w, open('queries_80.txt','w') as q:
    for line in f:
        count += 1
        sparql = json.loads(line)['sql'].replace("xmlschema","XMLSchema")

        sparql = clean_text(sparql)
        print(count, sparql)
        # q.write(sparql+'\n')

        start_time = time.time()
        sparql_res = kg.query(sparql)
        duration = time.time()-start_time

        for res in sparql_res:
            val = '|'
            temp = []
            for t in res:
                val += str(t.toPython()) + '|\t\t|'
                temp.append(str(t.toPython()))
            # print(val[:-1])
        
        duration2 = time.time()-start_time

        print(temp,duration*1000,duration2*1000)
        w.write(str(count)+',\"'+str(temp)+"\","+str(duration*1000)+','+str(duration2*1000)+'\n')