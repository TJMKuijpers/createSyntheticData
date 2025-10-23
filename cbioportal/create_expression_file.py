########################################################
#### File to create expression data synthetic data  ####
########################################################

import polars as pl
import numpy as np
from utils import get_patient_or_sample_identifiers, combine_dataframes_horizontal,read_gene_json

def create_expression_matrix(column_list,min_value,max_value,number_of_entries):
    names = column_list["SAMPLE_ID"].to_list()
    data = {
        name: np.random.randint(low=min_value, high=max_value, size=number_of_entries)
        for name in names
    }
    df = pl.DataFrame(data)
    return df

if __name__ == "__main__":
    gene_identifiers = read_gene_json('gene_identifiers.json',"entrezGeneId","hugoGeneSymbol")
    gene_identifiers_subset=gene_identifiers[0:1500,:]
    patient_identifiers = get_patient_or_sample_identifiers('data_clinical_sample.txt','\t','SAMPLE_ID')
    number_of_genes = gene_identifiers_subset.shape[0]
    print(number_of_genes)
    gene_expression_median = create_expression_matrix(patient_identifiers,2,15,number_of_genes)
    gene_expression_df = combine_dataframes_horizontal(gene_identifiers_subset,gene_expression_median)
    print(gene_expression_df.head())
    gene_expression_df.write_csv('data_gene_expression.txt',separator='\t')