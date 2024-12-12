from rdflib import Literal, XSD

COMPLEX_KG_SCHEMA = {
    'SUBJECT_ID': [
        'HADM_ID', 'GENDER', 'ANCHOR_AGE', 'ANCHOR_YEAR', 'ANCHOR_YEAR_GROUP',
        'DOD', 'LANGUAGE', 'RACE', 'HOSPITAL_EXPIRE_FLAG'
    ],
    'HADM_ID': [
        'ADMITTIME', 'DISCHTIME', 'DEATHTIME', 'ADMISSION_TYPE',
        'ADMIT_PROVIDER_ID', 'ADMISSION_LOCATION', 'DISCHARGE_LOCATION',
        'INSURANCE', 'LANGUAGE', 'MARITAL_STATUS', 'LOS',
        'DIAGNOSES', 'PROCEDURES', 'PRESCRIPTIONS', 'LAB', 'DISCHARGE', 'RADIOLOGY'
    ],
    'DIAGNOSES': [
        'DIAGNOSES_ICD_CODE', 'ICD_VERSION'
    ],
    'DIAGNOSES_ICD_CODE': [
        'DIAGNOSES_LONG_TITLE'
    ],
    'PROCEDURES': [
        'PROCEDURES_ICD_CODE', 'ICD_VERSION'
    ],
    'PROCEDURES_ICD_CODE': [
        'PROCEDURES_LONG_TITLE'
    ],
    'PRESCRIPTIONS': [
        'DRUG_TYPE', 'DRUG',
        'GSN', 'NDC', 'PROD_STRENGTH', 'FORM_RX', 'DOSE_VAL_RX', 'DOSE_UNIT_RX',
        'FORM_VAL_DISP', 'FORM_UNIT_DISP', 'DOSES_PER_24_HRS', 'ROUTE'
    ],
    'LAB': [
        'ITEMID', 'VALUE',
        'VALUENUM', 'VALUEUOM', 'REF_RANGE_LOWER', 'REF_RANGE_UPPER',
        'FLAG', 'COMMENTS', 'LABEL', 'FLUID', 'CATEGORY'
    ],
    'DISCHARGE': [
        'NOTE_TYPE', 'NOTE_SEQ', 'TEXT'
    ],
    'RADIOLOGY': [
        'NOTE_TYPE', 'NOTE_SEQ', 'TEXT'
    ]
}


patients_dtype = {
    'SUBJECT_ID': 'entity',
    'GENDER': XSD.string,
    'ANCHOR_AGE': XSD.integer,
    'ANCHOR_YEAR': XSD.integer,
    'ANCHOR_YEAR_GROUP': XSD.string,
    'DOD': XSD.dateTime,

}

admissions_dtype = {
    'SUBJECT_ID': 'entity',
    'HADM_ID': 'entity',
    'ADMITTIME': XSD.dateTime,
    'DISCHTIME': XSD.dateTime,
    'DEATHTIME': XSD.dateTime,
    'ADMISSION_TYPE': XSD.string,
    'INSURANCE': XSD.string,
    'MARITAL_STATUS': XSD.string,
    'LOS': XSD.integer,
    'LANGUAGE': XSD.string,
    'RACE': XSD.string,
    'HOSPITAL_EXPIRE_FLAG': XSD.integer
}

diagnoses_dtype = {
    'DIAGNOSES': 'entity', # key
    'HADM_ID': 'entity',
    'DIAGNOSES_ICD_CODE': 'entity',
    'ICD_VERSION': XSD.integer
}

d_icd_diagnoses_dtype = {
    'DIAGNOSES_ICD_CODE': 'entity',
    'DIAGNOSES_LONG_TITLE': XSD.string
}

procedures_dtype = {
    'PROCEDURES': 'entity',
    'HADM_ID': 'entity',
    'PROCEDURES_ICD_CODE': 'entity',
    'ICD_VERSION': XSD.integer
}

d_icd_procedures_dtype = {
    'PROCEDURES_ICD_CODE': 'entity',
    'PROCEDURES_LONG_TITLE': XSD.string
}

prescriptions_dtype = {
    'PRESCRIPTIONS': 'entity',
    'HADM_ID': 'entity',
    'DRUG_TYPE': XSD.string,
    'DRUG': XSD.string,
    'PROD_STRENGTH': XSD.string,
    'FORM_RX': XSD.string,
    'DOSE_VAL_RX': XSD.string,
    'DOSE_UNIT_RX': XSD.string,
    'FORM_VAL_DISP': XSD.string,
    'FORM_UNIT_DISP': XSD.string,
    'ROUTE': XSD.string
}

lab_dtype = {
    'LAB': 'entity',# key
    'HADM_ID': 'entity',
    'ITEMID': 'entity',
    'VALUE': XSD.string,
    'VALUENUM': XSD.float,
    'VALUEUOM': XSD.string,
    'REF_RANGE_LOWER': XSD.float,
    'REF_RANGE_UPPER': XSD.float,
    'FLAG': XSD.string,
    'COMMENTS': XSD.string
}

d_labitem_dtype = {
    'ITEMID': 'entity',
    'LABEL': XSD.string,
    'FLUID': XSD.string,
    'CATEGORY': XSD.string
}


discharge_dtype = {
    'DISCHARGE': 'entity',
    'HADM_ID': 'entity',
    'NOTE_TYPE': XSD.string,
    'TEXT': XSD.string
}

radiology_dtype = {
    'RADIOLOGY': 'entity',
    'HADM_ID': 'entity',
    'NOTE_TYPE': XSD.string,
    'TEXT': XSD.string
}

SIMPLE_SCHEMA_DTYPE = {
    **patients_dtype,
    **admissions_dtype,
    **diagnoses_dtype,
    **d_icd_diagnoses_dtype,
    **procedures_dtype,
    **d_icd_procedures_dtype,
    **prescriptions_dtype,
    **lab_dtype,
    **d_labitem_dtype,
    **radiology_dtype,
    **discharge_dtype
}

# print(len(demographic_dtype), len(diagnoses_dtype), len(prescriptions_dtype), len(procedures_dtype), len(lab_dtype))
#print(SCHEMA_DTYPE)