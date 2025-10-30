import polars as pl
import os
from utils import create_meta_data

def create_cancer_type(cancer_type_code,cancer_type,color,cancer):
    with open('/synthetic_data/data_cancer_type.txt', 'w') as file:
        file.write(f'{cancer_type_code}\t{cancer_type}\t{color}\t{cancer}')





if __name__ == '__main__':
    create_cancer_type('brca-test-study','Breast Invasive Carcinoma','HotPink','Breast')

    metadata_cancer_type = {
        "genetic_alteration_type": "CANCER_TYPE_GENE_EXPRESSION",
        "datatype": "mrna",
        "data_filename": "brca_tcga.txt"
    }

    create_meta_data(metadata_cancer_type, '/synthetic_data//meta_cancer_type.txt')
