from rdflib import Literal, XSD

SIMPLE_KG_SCHEMA = {
    'HADM_ID': [
        'SUBJECT_ID', 'GENDER', 'ANCHOR_AGE', 'ANCHOR_YEAR', 'ANCHOR_YEAR_GROUP',
        'DOD', 'ADMITTIME', 'DISCHTIME', 'DEATHTIME', 'ADMISSION_TYPE',
        'ADMIT_PROVIDER_ID', 'ADMISSION_LOCATION', 'DISCHARGE_LOCATION',
        'INSURANCE', 'LANGUAGE', 'MARITAL_STATUS', 'RACE', 'HOSPITAL_EXPIRE_FLAG', 'LOS'
    ],
    'DIAGNOSES': [
        'SUBJECT_ID', 'SEQ_NUM', 'DIAGNOSES_ICD_CODE', 'ICD_VERSION', 'DIAGNOSES_LONG_TITLE'
    ],
    'PROCEDURES': [
        'PROCEDURES', 'SUBJECT_ID', 'SEQ_NUM', 'CHARTDATE',
        'PROCEDURES_ICD9_CODE', 'ICD_VERSION', 'PROCEDURES_LONG_TITLE'
    ],
    'PRESCRIPTIONS': [
        'SUBJECT_ID', 'PHARMACY_ID', 'ORDER_PROVIDER_ID',
        'STARTTIME', 'STOPTIME', 'DRUG_TYPE', 'DRUG',
        'GSN', 'NDC', 'PROD_STRENGTH', 'FORM_RX', 'DOSE_VAL_RX', 'DOSE_UNIT_RX',
        'FORM_VAL_DISP', 'FORM_UNIT_DISP', 'DOSES_PER_24_HRS', 'ROUTE'
    ],
    'LAB': [
        'LABEVENT_ID', 'SUBJECT_ID', 'SPECIMEN_ID', 'ITEMID',
        'ORDER_PROVIDER_ID', 'CHARTTIME', 'STORETIME', 'VALUE',
        'VALUENUM', 'VALUEUOM', 'REF_RANGE_LOWER', 'REF_RANGE_UPPER',
        'FLAG', 'PRIORITY', 'COMMENTS', 'LABEL', 'FLUID', 'CATEGORY'
    ],
    'DISCHARGE': [
        'NOTE_ID', 'SUBJECT_ID', 'HADM_ID', 'NOTE_TYPE', 'NOTE_SEQ',
        'CHARTTIME', 'STORETIME', 'TEXT'
    ],
    'RADIOLOGY': [
        'NOTE_ID', 'SUBJECT_ID', 'HADM_ID', 'NOTE_TYPE', 'NOTE_SEQ',
        'CHARTTIME', 'STORETIME', 'TEXT'
    ]
}

demographic_dtype = {
    'SUBJECT_ID': 'entity',
    'GENDER': XSD.string,
    'ANCHOR_AGE': XSD.string,
    'ANCHOR_YEAR': XSD.string,
    'ANCHOR_YEAR_GROUP': XSD.string,
    'DOD': XSD.dateTime,
    'HADM_ID': 'entity',
    'ADMITTIME': XSD.dateTime,
    'DISCHTIME': XSD.dateTime,
    'DEATHTIME': XSD.dateTime,
    'ADMISSION_TYPE': XSD.string,
    'ADMIT_PROVIDER_ID': XSD.string,
    'ADMISSION_LOCATION': XSD.string,
    'DISCHARGE_LOCATION': XSD.string,
    'INSURANCE': XSD.string,
    'LANGUAGE': XSD.string,
    'MARITAL_STATUS': XSD.string,
    'RACE': XSD.string,
    'EDREGTIME': XSD.dateTime,
    'EDOUTTIME': XSD.dateTime,
    'HOSPITAL_EXPIRE_FLAG': XSD.integer,
    'LOS': XSD.integer
}

diagnoses_dtype = {
    'DIAGNOSES': 'entity', # key
    'HADM_ID': 'entity',
    'SEQ_NUM': XSD.string,
    'DIAGNOSES_ICD_CODE': 'entity',
    'ICD_VERSION': XSD.string,
    'DIAGNOSES_LONG_TITLE': XSD.string
}

procedures_dtype = {
    'PROCEDURES': 'entity',
    'HADM_ID': 'entity',
    'SEQ_NUM': XSD.string,
    'CHARTDATE': XSD.dateTime,
    'PROCEDURES_ICD_CODE': 'entity',
    'ICD_VERSION': XSD.string,
    'PROCEDURES_LONG_TITLE': XSD.string
}

prescriptions_dtype = {
    'PRESCRIPTIONS': 'entity',
    'HADM_ID': 'entity',
    'ORDER_PROVIDER_ID': XSD.string,
    'STARTTIME': XSD.dateTime,
    'STOPTIME': XSD.dateTime,
    'DRUG_TYPE': XSD.string,
    'DRUG': XSD.string,
    'GSN': XSD.string,
    'NDC': XSD.string,
    'PROD_STRENGTH': XSD.string,
    'FORM_RX': XSD.string,
    'DOSE_VAL_RX': XSD.string,
    'DOSE_UNIT_RX': XSD.string,
    'FORM_VAL_DISP': XSD.string,
    'FORM_UNIT_DISP': XSD.string,
    'DOSES_PER_24_HRS': XSD.string,
    'ROUTE': XSD.string
}

lab_dtype = {
    'LAB': 'entity',# key
    'HADM_ID': 'entity',
    'ORDER_PROVIDER_ID': XSD.string,
    'CHARTTIME': XSD.dateTime,
    'STORETIME': XSD.dateTime,
    'VALUE': XSD.string,
    'VALUENUM': XSD.float,
    'VALUEUOM': XSD.string,
    'REF_RANGE_LOWER': XSD.float,
    'REF_RANGE_UPPER': XSD.float,
    'FLAG': XSD.string,
    'PRIORITY': XSD.string,
    'COMMENTS': XSD.string,
    'LABEL': XSD.string,
    'FLUID': XSD.string,
    'CATEGORY': XSD.string
}


discharge_dtype = {
    'DISCHARGE': 'entity',
    # 'SUBJECT_ID': 'entity',
    'HADM_ID': 'entity',
    'NOTE_TYPE': XSD.string,
    'NOTE_SEQ': XSD.integer,
    'CHARTTIME': XSD.dateTime,
    'STORETIME': XSD.dateTime,
    'TEXT': XSD.string
}

radiology_dtype = {
    'RADIOLOGY': 'entity',
    # 'SUBJECT_ID': 'entity',
    'HADM_ID': 'entity',
    'NOTE_TYPE': XSD.string,
    'NOTE_SEQ': XSD.integer,
    'CHARTTIME': XSD.dateTime,
    'STORETIME': XSD.dateTime,
    'TEXT': XSD.string
}

SIMPLE_SCHEMA_DTYPE = {
    **demographic_dtype,
    **diagnoses_dtype,
    **procedures_dtype,
    **prescriptions_dtype,
    **lab_dtype,
    **radiology_dtype,
    **discharge_dtype
}

# print(len(demographic_dtype), len(diagnoses_dtype), len(prescriptions_dtype), len(procedures_dtype), len(lab_dtype))
#print(SCHEMA_DTYPE)