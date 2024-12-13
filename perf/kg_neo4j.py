import json
import time
from neo4j import GraphDatabase

URI = "neo4j://localhost" #REQUIRES NEO4J CONNECTION
print("neo4j connected")

with GraphDatabase.driver(URI) as driver:
    driver.verify_connectivity()

with open('/data3/ams560-f24/project/perf/neo4j_queries.txt') as f:
    for query in f:
        records,summary,keys = driver.execute_query(query)
        print(records, "," , summary.result_available_after , "," , summary.result_consumed_after)
