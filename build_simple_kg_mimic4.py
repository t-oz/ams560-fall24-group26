import sys
sys.path.append('..')
sys.path.append('.')
import os
from rdflib import Graph, URIRef
import sqlite3
import pandas as pd
from rdflib import Literal
from kg_simple_schema import *
import time

start = time.time()

domain = ''
triples = []

def isNoneNan(val):
    if val is None:
        return True

    if (type(val) == str) and (val.lower() in ['none', 'nan', '']):
        return True

    if val != val:
        return True

    return False


def clean_text(val):
    if type(val) == str:
        val = val.replace("\\", ' ')
    return val

def wrap2uri(obj, literal_type):
    obj = obj.lower()
    if literal_type == 'entity':
        return URIRef(obj)

    elif literal_type == 'relation':
        return URIRef(obj)

    else:
        return Literal(clean_text(obj), datatype=literal_type)

def table2triples(df, parent_col, subject_col, col_types):
    triples = []
    for col_name, _ in col_types.items():

        if col_name == parent_col:
            triples += [(wrap2uri(f'{domain}/{col_name}/{sub}', col_types[parent_col]),
                         wrap2uri(f'{domain}/{subject_col}', 'relation'),
                         wrap2uri(f'{domain}/{subject_col}/{obj}', col_types[subject_col]))
                        for (sub, obj) in zip(df[col_name], df[subject_col])]
            continue

        if col_name == subject_col:
            continue

        for (sub, obj) in zip(df[subject_col], df[col_name]):

            if isNoneNan(obj):
                continue
            triple_to_add = [(wrap2uri(f'{domain}/{subject_col}/{sub}', col_types[subject_col]),
                         wrap2uri(f'{domain}/{col_name}', 'relation'),
                         wrap2uri(f'{domain}/{col_name}/{obj}' if col_types[col_name] == 'entity' else f'{obj}', col_types[col_name]))]
            triples += triple_to_add

    return triples

if __name__ == '__main__':
    print('Building simple MIMIC-IV knowledge graph...')
    print('Loading patient IDs...')
    patient_ids = pd.read_csv('5_patient_ids.csv', header=None).iloc[:, 0].tolist()
    id_list_str = ', '.join(map(str, patient_ids))
    print(id_list_str)

    print('Connecting to database...')
    db_conn = sqlite3.connect('/data3/ams560-f24/mimic_iv/mimic4.db')

    print('Building demographic dataframe...')
    dmographic = pd.read_sql_query(f"""select * from 'hosp/patients' pat join 'hosp/admissions' adm
             on pat.subject_id = adm.subject_id
             where pat.subject_id in ({id_list_str})
             order by pat.subject_id, adm.admittime""", db_conn)
    dmographic.columns = dmographic.columns.str.upper()
    print(dmographic.head())

    print('Building diagnoses dataframe...')
    query = f"""select o.*, t.long_title from 'hosp/diagnoses_icd' o join 'hosp/d_icd_diagnoses' t
            on o.icd_code = t.icd_code and o.icd_version = t.icd_version
            where o.subject_id in ({id_list_str});"""
    diagnoses = pd.read_sql_query(query, db_conn)
    diagnoses.columns = diagnoses.columns.str.upper()
    diagnoses = diagnoses.reset_index().rename({'index': 'DIAGNOSES',
                                                'ICD_CODE': 'DIAGNOSES_ICD_CODE',
                                                'LONG_TITLE': 'DIAGNOSES_LONG_TITLE'}, axis=1)

    print('Building procedures dataframe...')
    query = f"""select o.*, t.long_title from 'hosp/procedures_icd' o join 'hosp/d_icd_procedures' t
            on o.icd_code = t.icd_code and o.icd_version = t.icd_version
            where o.subject_id in ({id_list_str});"""
    procedures = pd.read_sql_query(query, db_conn)
    procedures.columns = procedures.columns.str.upper()
    procedures = procedures.reset_index().rename({'index': 'PROCEDURES',
                                                  'ICD_CODE': 'PROCEDURES_ICD_CODE',
                                                  'LONG_TITLE': 'PROCEDURES_LONG_TITLE'}, axis=1)

    print('Building prescriptions dataframe...')
    query = f"""select * from 'hosp/prescriptions' where subject_id in ({id_list_str})"""
    prescriptions = pd.read_sql_query(query, db_conn)
    prescriptions = prescriptions.reset_index().rename({'index': 'PRESCRIPTIONS'}, axis=1)
    prescriptions.columns = prescriptions.columns.str.upper()

    print('Building labs dataframe...')
    query = f"""select * from 'hosp/labevents' o join 'hosp/d_labitems' t
    on o.itemid = t.itemid
    where o.subject_id in ({id_list_str}) and o.hadm_id > 0;"""
    lab = pd.read_sql_query(query, db_conn)
    lab = lab.reset_index().rename({'index': 'LAB'}, axis=1)
    lab.columns = lab.columns.str.upper()

    print('Building discharge summary dataframe...')
    query = f"""select * from 'notes/discharge'
    where subject_id in ({id_list_str});"""
    discharge = pd.read_sql_query(query, db_conn)
    discharge = discharge.reset_index().rename({'index': 'DISCHARGE'}, axis=1)
    discharge.columns = discharge.columns.str.upper()

    print('Building radiology dataframe...')
    query = f"""select * from 'notes/radiology'
    where subject_id in ({id_list_str}) and hadm_id > 0;"""

    radiology = pd.read_sql_query(query, db_conn)
    radiology = radiology.reset_index().rename({'index': 'RADIOLOGY'}, axis=1)
    radiology.columns = radiology.columns.str.upper()

    print('Dataframes loaded.')
    print('Converting dataframes to KG triples...')
    triples += table2triples(dmographic, parent_col='', subject_col='HADM_ID', col_types=demographic_dtype)
    triples += table2triples(diagnoses, parent_col='HADM_ID', subject_col='DIAGNOSES', col_types=diagnoses_dtype)
    triples += table2triples(procedures, parent_col='HADM_ID', subject_col='PROCEDURES', col_types=procedures_dtype)
    triples += table2triples(prescriptions, parent_col='HADM_ID', subject_col='PRESCRIPTIONS',
                             col_types=prescriptions_dtype)
    triples += table2triples(lab, parent_col='HADM_ID', subject_col='LAB', col_types=lab_dtype)
    triples += table2triples(discharge, parent_col='HADM_ID', subject_col='DISCHARGE', col_types=discharge_dtype)
    triples += table2triples(radiology, parent_col='HADM_ID', subject_col='RADIOLOGY', col_types=radiology_dtype)

    print('Triple conversion complete.')
    print(f'Total: {len(triples)} triples.')

    print('Creating knowledge graph...')
    kg = Graph()
    for i, triple in enumerate(triples):
        kg.add(triple)
    kg.serialize(destination='mimic4_simple_kg.xml', format='xml')

    print(f'Done. Runtime: {int(time.time() - start)} seconds.')