import polars as pl
import os
from utils import get_patient_or_sample_identifiers, replace_sample_ids, duplicate_rows,create_categorical_values,combine_dataframes_horizontal


def create_resource_data():
    patient_ids = get_patient_or_sample_identifiers(os.path.join(os.getcwd(),'synthetic_data/data_clinical_patient.txt'),sep='\t', select_column='PATIENT_ID',2)["PATIENT_ID"].to_list()
    patient_resource_id = create_categorical_values(patient_ids.__len__(), ['PATIENT_NOTES'], 'RESOURCE_ID')
    patient_resource_url = create_categorical_values(patient_ids.__len__(), ['http://url-to-none-existing'], 'URL')

    patient_resource_df=combine_dataframes_horizontal(pl.DataFrame({'PATIENT_ID':patient_ids}),patient_resource_id,patient_resource_url)

    sample_patient_ids = get_patient_or_sample_identifiers(os.path.join(os.getcwd(), 'synthetic_data/data_clinical_sample.txt'),sep='\t', select_column=['PATIENT_ID', 'SAMPLE_ID'])
    sample_resource_url = create_categorical_values(sample_patient_ids.shape[0], ['http://url-to-none-existing'], 'URL')
    sample_resource_id = create_categorical_values(sample_patient_ids.shape[0], ['PATHOLOGY_SLIDE'],
                                                     'RESOURCE_ID')

    sample_resource_df = combine_dataframes_horizontal(sample_patient_ids, sample_resource_id,
                                                        sample_resource_url)

    sample_resource_df.write_csv(os.path.join(os.getcwd(),'synthetic_data/resouce_data_sample.txt'), separator="\t")
    patient_resource_df.write_csv(os.path.join(os.getcwd(), 'synthetic_data/resouce_data_patient.txt'), separator="\t")

if __name__ == "__main__":
    create_resource_data()
