########################################################
#### File to create expression data synthetic data  ####
########################################################

import polars as pl
import os
from utils import get_patient_or_sample_identifiers, combine_dataframes_horizontal,read_gene_json,create_expression_matrix

if __name__ == "__main__":
    gene_identifiers = read_gene_json('gene_identifiers.json',"entrezGeneId","hugoGeneSymbol")
    gene_identifiers_subset=gene_identifiers[0:1500,:]
    gene_identifiers_subset= gene_identifiers_subset.filter(pl.col('entrezGeneId')>=0)
    patient_identifiers = get_patient_or_sample_identifiers(os.path.join(os.getcwd(), 'synthetic_data/data_clinical_sample.txt'),'\t','SAMPLE_ID',4)
    number_of_genes = gene_identifiers_subset.shape[0]
    gene_expression_median = create_expression_matrix(patient_identifiers,'SAMPLE_ID',2,15,number_of_genes,'EXPR')
    gene_expression_df = combine_dataframes_horizontal(gene_identifiers_subset,gene_expression_median)
    gene_expression_df = gene_expression_df.rename({'entrezGeneId':"Entrez_Gene_Id",'hugoGeneSymbol':"Hugo_Symbol"})
    gene_expression_df.write_csv('data_expression_continuous.txt',separator='\t')