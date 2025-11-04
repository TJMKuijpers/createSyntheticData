import polars as pl
import os
from utils import get_patient_or_sample_identifiers, combine_dataframes_horizontal,create_categorical_matrix


def create_cna_armlevel(reference_data,samples,categories):
    armlevel_martrix=create_categorical_matrix(samples,'SAMPLE_ID',categories,reference_data.shape[0])
    df=combine_dataframes_horizontal(reference_data,armlevel_martrix)
    return df

if __name__ == "__main__":
    example_data = pl.read_csv(os.path.join(os.getcwd(), "example_data/data_armlevel_cna.txt"), separator='\t').select(['ENTITY_STABLE_ID','NAME','DESCRIPTION'])
    sample_idenifiers = get_patient_or_sample_identifiers(os.path.join(os.getcwd(), 'synthetic_data/data_clinical_samples.txt'),'\t','SAMPLE_ID',2)
    categories = ['Loss', 'Gain', 'Na', 'Unchanged']
    data=create_cna_armlevel(example_data,sample_idenifiers,categories)
    data.write_csv(os.path.join(os.getcwd(), 'synthetic_data/data_armlevel_cna.txt'),separator='\t')