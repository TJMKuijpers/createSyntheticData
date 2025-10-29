########################################################
#### File to create expression data synthetic data  ####
########################################################

import polars as pl
import os
from utils import get_patient_or_sample_identifiers, combine_dataframes_horizontal,read_gene_json,create_expression_matrix

if __name__ == "__main__":
    gene_identifiers = read_gene_json('gene_identifiers.json',"entrezGeneId","hugoGeneSymbol")
    gene_identifiers_subset=gene_identifiers[0:1500,:]
    patient_identifiers = get_patient_or_sample_identifiers(os.path.join(os.getcwd(), 'syntethic_data/data_clinical_sample.txt'),'\t','SAMPLE_ID')
    number_of_genes = gene_identifiers_subset.shape[0]
    print(number_of_genes)
    gene_expression_median = create_expression_matrix(patient_identifiers,'SAMPLE_ID',2,15,number_of_genes,'EXPR')
    gene_expression_df = combine_dataframes_horizontal(gene_identifiers_subset,gene_expression_median)
    print(gene_expression_df.head())
    gene_expression_df.write_csv('data_gene_expression.txt',separator='\t')