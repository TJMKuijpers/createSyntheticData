import polars as pl
import os
from utils import get_patient_or_sample_identifiers, combine_dataframes_horizontal,read_gene_json,create_expression_matrix


if __name__ == "__main__":
    reference_id_counts= pl.read_csv(os.path.join(os.getcwd(),'example_data/data_mutational_signatures_counts_ID.txt'),separator='\t')
    reference_id_contribution = pl.read_csv(os.path.join(os.getcwd(),'example_data/data_mutational_signatures_contribution_ID.txt'),separator='\t')
    reference_sbs_counts= pl.read_csv(os.path.join(os.getcwd(),'example_data/data_mutational_signatures_counts_SBS.txt'),separator='\t')
    reference_sbs_contribution = pl.read_csv(os.path.join(os.getcwd(),'example_data/data_mutational_signatures_contribution_SBS.txt'),separator='\t')
    reference_dbs_counts= pl.read_csv(os.path.join(os.getcwd(),'example_data/data_mutational_signatures_counts_DBS.txt'),separator='\t')
    reference_dbs_contribution = pl.read_csv(os.path.join(os.getcwd(),'example_data/data_mutational_signatures_contribution_DBS.txt'),separator='\t')

    sample_idenifiers = get_patient_or_sample_identifiers(os.path.join(os.getcwd(), 'synthetic_data/data_clinical_sample.txt'),'\t','SAMPLE_ID',4)

    sbs_contributions=create_expression_matrix(sample_idenifiers,'SAMPLE_ID',0,1,reference_sbs_contribution.shape[0],"CONTRIBUTION")
    sbs_counts=create_expression_matrix(sample_idenifiers,'SAMPLE_ID',0,40,reference_sbs_counts.shape[0],"COUNT")
    dbs_contributions = create_expression_matrix(sample_idenifiers, 'SAMPLE_ID', 0, 1, reference_dbs_contribution.shape[0],
                                               "CONTRIBUTION")
    dbs_counts = create_expression_matrix(sample_idenifiers, 'SAMPLE_ID', 0, 40, reference_dbs_counts.shape[0], "COUNT")
    id_contributions = create_expression_matrix(sample_idenifiers, 'SAMPLE_ID', 0, 1, reference_id_contribution.shape[0],
                                               "CONTRIBUTION")
    id_counts = create_expression_matrix(sample_idenifiers, 'SAMPLE_ID', 0, 40, reference_id_counts.shape[0], "COUNT")

    sbs_contribution_data=combine_dataframes_horizontal(reference_sbs_contribution.select(["ENTITY_STABLE_ID","NAME","DESCRIPTION","URL"]),sbs_contributions)
    sbs_counts_data = combine_dataframes_horizontal(
        reference_sbs_counts.select(["ENTITY_STABLE_ID", "NAME"]), sbs_counts)

    dbs_contribution_data=combine_dataframes_horizontal(reference_sbs_contribution.select(["ENTITY_STABLE_ID","NAME","DESCRIPTION","URL"]),dbs_contributions)
    dbs_counts_data=combine_dataframes_horizontal(
        reference_dbs_counts.select(["ENTITY_STABLE_ID", "NAME"]), dbs_counts)
    id_contribution_data =combine_dataframes_horizontal(reference_sbs_contribution.select(["ENTITY_STABLE_ID","NAME","DESCRIPTION","URL"]),id_contributions)
    id_counts_data =combine_dataframes_horizontal(
        reference_id_counts.select(["ENTITY_STABLE_ID", "NAME"]), id_counts)

    sbs_contribution_data.write_csv(os.path.join(os.getcwd(),'synthetic_data/data_mutational_signatures_contribution_SBS.txt'),separator='\t')
    dbs_contribution_data.write_csv(os.path.join(os.getcwd(),'synthetic_data/data_mutational_signatures_contribution_DBS.txt'), separator='\t')
    id_contribution_data.write_csv(os.path.join(os.getcwd(),'synthetic_data/data_mutational_signatures_contribution_ID.txt'), separator='\t')

    sbs_counts_data.write_csv(os.path.join(os.getcwd(),'synthetic_data/data_mutational_signatures_counts_SBS.txt'),separator='\t')
    dbs_counts_data.write_csv(os.path.join(os.getcwd(),'synthetic_data/data_mutational_signatures_counts_DBS.txt'),separator='\t')
    id_counts_data.write_csv(os.path.join(os.getcwd(),'synthetic_data/data_mutational_signatures_counts_ID.txt'),separator='\t')