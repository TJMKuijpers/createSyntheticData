import polars as pl
import os
from utils import get_patient_or_sample_identifiers,create_expression_matrix,combine_dataframes_horizontal


def create_gsva_data():
    gsva_geneset=pl.read_csv(os.path.join(os.getcwd(),'/synthetic_data//genesets.gmt'),separator='\t',has_header=False).select('column_1')
    sample_patient_ids = get_patient_or_sample_identifiers(os.path.join(os.getcwd(), 'synthetic_data/data_clinical_sample.txt'),sep='\t', select_column=['PATIENT_ID', 'SAMPLE_ID'],2)
    pvalue_matrix = create_expression_matrix(sample_patient_ids,'SAMPLE_ID',0,1,gsva_geneset.__len__(),'PVALUE')
    score_matrix = create_expression_matrix(sample_patient_ids,'SAMPLE_ID',-1,1,gsva_geneset.__len__(),'SCORE')
    gsva_pvalue_df = combine_dataframes_horizontal(gsva_geneset,pvalue_matrix).rename({'column_1': 'geneset_id'})
    gsva_scores_df = combine_dataframes_horizontal(gsva_geneset,score_matrix).rename({'column_1': 'geneset_id'})
    gsva_pvalue_df.write_csv(os.path.join(os.getcwd(), '/synthetic_data//data_gsva_pvalues.txt'), separator="\t")
    gsva_scores_df.write_csv(os.path.join(os.getcwd(), '/synthetic_data//data_gsva_scores.txt'), separator="\t")
    print(gsva_scores_df.head())

if __name__ == "__main__":
    create_gsva_data()
