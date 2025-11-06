import polars as pl
import os
from utils import get_patient_or_sample_identifiers, replace_sample_ids, duplicate_rows, add_custom_namespace_cols


def main():
    df = pl.read_csv(os.path.join(os.getcwd(), "example_data/data_mutations_msk_ch_2023.txt"), separator='\t')
    sample_ids = get_patient_or_sample_identifiers(os.path.join(os.getcwd(), 'synthetic_data/data_clinical_sample.txt'),'\t','SAMPLE_ID',4)
    df.drop('Tumor_Sample_Barcode')
    df = replace_sample_ids(df, sample_ids['SAMPLE_ID'].to_list(), sample_col='Tumor_Sample_Barcode')
    df = duplicate_rows(df, sample_ids.shape[0])
    df = add_custom_namespace_cols(df)
    df.write_csv('data_mutations.txt', separator="\t")

if __name__ == "__main__":
    main()
