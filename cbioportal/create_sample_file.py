###############################################################
#### Python script to create clinical data on  sample level ###
###############################################################
# Author: T.J.M. Kuijpers

# Columns in sample file:
# PATIENT_ID
# SAMPLE_ID
# SUBTYPE

import polars as pl
import polars.selectors as cs
import numpy as np
from utils import get_patient_or_sample_identifiers, create_categorical_values,create_numerical_values,combine_dataframes_horizontal


def create_samples_for_patient(patient_ids: list[str], number_of_samples: int) -> pl.DataFrame:
    num_patients = len(patient_ids)
    patient_ids_duplicated=pl.DataFrame(np.repeat(patient_ids['PATIENT_ID'].to_list(),3,axis=0))
    patient_ids=patient_ids['PATIENT_ID'].to_list()
    samples=[]
    for y in range(0,patient_ids.__len__()):
        for x in range(1,number_of_samples+1):
            samples.append(f"{patient_ids[y]}-S-{x}")

    df = pl.DataFrame({
        'PATIENT_ID': patient_ids_duplicated,
        'SAMPLE_ID': samples
    })
    return df



if __name__ == "__main__":
   number_of_patients=100000
   number_of_samples=3
   total_size=number_of_patients*number_of_samples
   subtype=create_categorical_values(total_size,['basal-like','NA','Her2 enriched','Luminal A','Luminal B'],'SUBTYPE')
   cancer=create_categorical_values(total_size,['Colorectal Cancer'],'CANCER_TYPE')
   st = create_categorical_values(total_size,['Primary Tumor'],'SAMPLE_TYPE')
   somatic = create_categorical_values(total_size, ['MATCHED'], 'SOMATIC STATUS')
   cancer_detail= create_categorical_values(total_size, ['Colon Adenocarcinoma'], 'CANCER_TYPE_DETAILED')
   tmb = create_numerical_values(total_size,1,50,2,'TMB')
   patient_data=get_patient_or_sample_identifiers('synthetic_data/data_clinical_patient.txt', sep='\t', select_column='PATIENT_ID', skip_lines=4)
   patient_sample_df=create_samples_for_patient(patient_data,3)
   sample_file=combine_dataframes_horizontal(patient_sample_df,subtype)
   sample_file = combine_dataframes_horizontal(sample_file, cancer)
   sample_file = combine_dataframes_horizontal(sample_file, st)
   sample_file = combine_dataframes_horizontal(sample_file, somatic)
   sample_file = combine_dataframes_horizontal(sample_file, cancer_detail)
   sample_file = combine_dataframes_horizontal(sample_file, tmb)
   #sample_file.with_columns((~cs.string()).cast(pl.String))

   clinical_sample_type = pl.DataFrame(
       {"col1": '#STRING', "col2": 'STRING', "col3": 'STRING', "col4": 'STRING', "col15": 'STRING', "col6": 'STRING',
        "col7": 'STRING',"col8":"STRING"})
   clinical_sample_order = pl.DataFrame(
       {"col1": '#1', "col2": 2, "col3": 3, "col4": 4, "col15": 5, "col6": 6,
        "col7": 7, "col8": 8})
   clinical_sample_comment = pl.DataFrame(
       {"col1": "#Patient Id", "col2": "Sample Id", "col3": 'Subtype', "col4": 'Cancer type',
        "col5": 'Sample type', "col6":'Somatic status',"col7": 'Cancer type detailed',"col8":"TMB"})

   output_file = "synthetic_data/data_clinical_sample.txt"
   with open(output_file, mode="a") as f:
       clinical_sample_comment.write_csv(f, separator='\t', include_header=False)
       clinical_sample_comment.write_csv(f, separator='\t', include_header=False)
       clinical_sample_type.write_csv(f, separator='\t', include_header=False)
       clinical_sample_order.write_csv(f, separator='\t', include_header=False)
       sample_file.write_csv(f,separator='\t', include_header=True)

