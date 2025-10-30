import polars as pl
import os
from utils import get_patient_or_sample_identifiers,create_expression_matrix,combine_dataframes_horizontal


def create_resource_data():
    sample_patient_ids = get_patient_or_sample_identifiers(os.path.join(os.getcwd(), 'synthetic_data/data_clinical_sample.txt'),sep='\t', select_column=['PATIENT_ID', 'SAMPLE_ID'],2)
    reference_rppa_elements_data= pl.read_csv(os.path.join(os.getcwd(),'example_data/data_rppa_acc_tcga.txt'),separator='\t').select('Composite.Element.REF')
    fake_rppa_data= create_expression_matrix(sample_patient_ids,'SAMPLE_ID',-2,2,reference_rppa_elements_data.shape[0],'RPPA')

    fake_rppa_df=combine_dataframes_horizontal(reference_rppa_elements_data,fake_rppa_data)
    fake_rppa_df.write_csv(os.path.join(os.getcwd(), 'synthetic_data/data_rppa.txt'), separator="\t")

if __name__ == "__main__":
    create_resource_data()
