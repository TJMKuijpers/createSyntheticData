########################################################
#### File to create expression data synthetic data  ####
########################################################

import polars as pl
import numpy as np
from utils import get_patient_identifiers, combine_dataframes_horizontal

def create_expression_matrix(column_list,min_value,max_value,number_of_entries):
    names = column_list["PATIENT_ID"].to_list()
    data = {
        name: np.random.randint(low=min_value, high=max_value, size=number_of_entries)
        for name in names
    }
    df = pl.DataFrame(data)
    return df

def read_gene_json(input_json):
    df = pl.read_json(input_json)
    return df.select(["entrezGeneId","hugoGeneSymbol"])




if __name__ == "__main__":
    gene_identifiers = read_gene_json('gene_identifiers.json')
    gene_identifiers_subset=gene_identifiers[0:1500,:]
    patient_identifiers = get_patient_identifiers('data_clinical_patient.txt','\t')
    number_of_genes = gene_identifiers_subset.shape[0]
    print(number_of_genes)
    gene_expression_median = create_expression_matrix(patient_identifiers,2,15,number_of_genes)
    gene_expression_df = combine_dataframes_horizontal(gene_identifiers_subset,gene_expression_median)
    print(gene_expression_df.head())
    gene_expression_df.write_csv('data_gene_expression.txt',separator='\t')