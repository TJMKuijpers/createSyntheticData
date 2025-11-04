import polars as pl
import os
from utils import get_patient_or_sample_identifiers, combine_dataframes_horizontal,create_expression_matrix


def create_treatment_data(reference_data,samples):
    treatment_martrix=create_expression_matrix(samples,'SAMPLE_ID',0,8,reference_data.shape[0],'TREATMENT')
    df=combine_dataframes_horizontal(reference_data,treatment_martrix)
    return df

if __name__ == "__main__":
    example_data = pl.read_csv(os.path.join(os.getcwd(), "example_data/data_treatment_ic50.txt"), separator='\t').select(['ENTITY_STABLE_ID','NAME','DESCRIPTION','URL'])
    sample_idenifiers = get_patient_or_sample_identifiers(os.path.join(os.getcwd(), 'synthetic_data/data_clinical_sample.txt'),'\t','SAMPLE_ID',4)
    data=create_treatment_data(example_data,sample_idenifiers)
    data.write_csv(os.path.join(os.getcwd(), 'synthetic_data/data_treatment_ic50.txt'),separator='\t')