##########################################################################
#### Python script to create clinical data on patient and sample level ###
##########################################################################
# Author: T.J.M. Kuijpers

# Columns in patient file:
# Patient Identifier
# Overall Survival
# Status Overall Survival (Months)
# Disease Free Status Disease Free (Months)

import random
import polars as pl
import polars.selectors as cs


def create_patient_identifier(patient_size):
    identifier_list = []
    base_string = 'Fake-Patient-'  # Added a hyphen to match your desired output format
    for x in range(1, patient_size + 1):  # Start at 1 and go up to and including patient_size
        # Append the new identifier to the list
        identifier_list.append(base_string + str(x))
    return identifier_list


def create_categorical_list_patients(patient_size,option_list):
    # Randomize survival status 1:Deceased and 0:Living
    return [random.choice(option_list) for i in range(0,patient_size)]

def create_numerical_list_patients(patient_size,min_value,max_value,number_of_decimals):
    return [round(random.uniform(min_value, max_value), number_of_decimals)  for i in range(patient_size)]

if __name__ == "__main__":
    patient_id=create_patient_identifier(1000000)
    os_options=['0:Living','1:Deceased','NA']
    dfs_options=['0:DiseaseFree','1:Recurred/Progressed','NA']
    os_status=create_categorical_list_patients(1000000,os_options)
    dfs_status=create_categorical_list_patients(1000000,dfs_options)
    os_months=create_numerical_list_patients(1000000,10,100,2)
    dfs_months=create_numerical_list_patients(1000000,15,80,2)
    age=create_numerical_list_patients(1000000,10,100,0)
    sex=create_categorical_list_patients(1000000,['Male','Female'])
    cancer_type=create_categorical_list_patients(1000000,['Breast Cancer','Prostate Cancer','Pancreatic Cancer','Non-Small Cell Lung Cancer'])
    data_frame = pl.DataFrame({'PATIENT_ID':patient_id,'AGE':age,'OS_STATUS':os_status,'OS_MONTHS':os_months,'DFS_STATUS':dfs_status,'DFS_MONTHS':dfs_months,'CANCER_TYPE':cancer_type})
    data_frame.with_columns((~cs.string()).cast(pl.String))
    data_frame.write_csv('data_clinical_patient.txt',separator='\t')