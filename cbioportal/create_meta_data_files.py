cancer_study_id = "fake_clickhouse_100k"
study_name = "Dataset 100.000 samples"
study_description = "Fake dataset to test endpoints for clickhouse"
type_of_cancer = "brca-test-study"
from utils import create_meta_data
# Create meta data
meta_cna_discrete = {
    "cancer_study_identifier": f"{cancer_study_id}",
     "genetic_alteration_type": "COPY_NUMBER_ALTERATION",
     "datatype": "DISCRETE",
     "stable_id": "gistic",
     "show_profile_in_analysis_tab": "true",
     "profile_description": "Putative copy-number from GISTIC 2.0. Values: -2 = homozygous deletion; -1 = hemizygous deletion; 0 = neutral / no change; 1 = gain; 2 = high level amplification.",
     "profile_name": "Putative copy-number alterations from GISTIC",
     "data_filename": "data_cna_discrete.txt",
}
meta_cna_log2 = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "COPY_NUMBER_ALTERATION",
"datatype": "LOG2-VALUE",
"stable_id": "log2CNA",
"show_profile_in_analysis_tab": "false",
"profile_description": "Log2 copy-number values for each gene (from Affymetrix SNP6).",
"profile_name": "Log2 copy-number values",
"data_filename": "data_cna_log2.txt"
}

meta_cna_hg19 = {
 "cancer_study_identifier": f"{cancer_study_id}",
 "genetic_alteration_type": "COPY_NUMBER_ALTERATION",
 "datatype": "SEG",
 "reference_genome_id": "hg19",
 "description": "Somatic CNA data (copy number ratio from tumor samples minus ratio from matched normals) from TCGA.",
 "data_filename": "data_cna_hg19.seg"
}

meta_gsva_scores = {
"cancer_study_identifier": f"{cancer_study_id}",
'genetic_alteration_type': "GENESET_SCORE",
"datatype": "GSVA-SCORE",
"stable_id": "gsva_scores",
"source_stable_id": "mrna",
"profile_name": "GSVA scores on oncogenic signatures gene sets",
"profile_description": "GSVA scores using mRNA expression data",
'data_filename': "data_gsva_scores.txt",
"show_profile_in_analysis_tab": "true",
"geneset_def_version": "msigdb_7.5.1"
}

meta_gsva_pvalues = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "GENESET_SCORE",
"datatype": "P-VALUE",
"stable_id": "gsva_pvalues",
"source_stable_id": "gsva_scores",
"profile_name": "Pvalues of GSVA scores on oncogenic signatures gene sets",
"profile_description": "Pvalues GSVA scores using mRNA expression data",
"data_filename": "data_gsva_pvalues.txt",
"geneset_def_version": "msigdb_7.5.1"

}
meta_clinical_patients = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "CLINICAL",
"datatype": "PATIENT_ATTRIBUTES",
"data_filename": "data_clinical_patient.txt"
}

meta_clinical_samples = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "CLINICAL",
"datatype": "SAMPLE_ATTRIBUTES",
"data_filename": "data_clinical_sample.txt"
}

meta_structural_variants = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "STRUCTURAL_VARIANT",
"datatype": "SV",
"data_filename": "data_structural_variants.txt",
"stable_id": "structural_variants",
"profile_name": "Targeted Fusion Assay data (Fake data)",
"profile_description": "Targeted Fusion Assay data created by The Hyve",
"show_profile_in_analysis_tab": "true",
}

meta_methylation_hm27 = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "METHYLATION",
"datatype": "CONTINUOUS",
"stable_id": "methylation_hm27",
"profile_description": "Methylation beta-values (HM27 platform). For genes with multiple methylation probes, the probe least correlated with expression is selected.",
"show_profile_in_analysis_tab": "false",
"profile_name": "Methylation (HM27)",
"data_filename": "data_methylation_hm27.txt"
}

meta_study = {
"type_of_cancer": f"{type_of_cancer}",
"cancer_study_identifier": f"{cancer_study_id}",
"name": f"{study_name}",
"description": f"{study_description}",
"citation": "Cell 2018",
"pmid": "29625048,29596782,29622463,29617662,29625055,29625050",
"groups": "PUBLIC",
"add_global_case_list": "true",
"tags_file": "study_tags.yml",
"reference_genome": "hg19"
}

meta_treatment_ic50 ={
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "GENERIC_ASSAY",
"generic_assay_type": "TREATMENT_RESPONSE",
"datatype": "LIMIT-VALUE",
"stable_id": "treatment_ic50",
"profile_name": "IC50 values of compounds on cellular phenotype readout",
"profile_description": "IC50 (compound concentration resulting in half maximal inhibition) of compounds on cellular phenotype readout of cultured mutant cell lines.",
"data_filename": "data_treatment_ic50.txt",
"show_profile_in_analysis_tab": "true",
"pivot_threshold_value": "0.1",
"value_sort_order": "ASC"
}

meta_expression_continuous = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "MRNA_EXPRESSION",
"datatype": "CONTINUOUS",
"stable_id": "rna_seq_mrna",
"profile_description": "Fake RNA data",
"show_profile_in_analysis_tab": "false",
"profile_name": "mRNA expression",
"data_filename": "data_expression_continuous.txt"
}

meta_expression_median = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "MRNA_EXPRESSION",
"datatype": "CONTINUOUS",
"stable_id": "mrna",
"profile_description": "Expression levels (Agilent microarray).",
"show_profile_in_analysis_tab": "false",
"profile_name": "mRNA expression (microarray)",
"data_filename": "data_expression_median.txt"
}

meta_mutational_signatures_sbs_counts ={
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "GENERIC_ASSAY",
"generic_assay_type": "MUTATIONAL_SIGNATURE",
"datatype": "LIMIT-VALUE",
"stable_id": "mutational_signature_sbs",
"profile_name": "generic assay test profile SBS",
"profile_description": "test profile for generic assay",
"data_filename": "data_mutational_signatures_counts_SBS.txt",
"generic_entity_meta_properties": "NAME",
"show_profile_in_analysis_tab": "true"
}

meta_mutational_signatures_dbs_counts ={
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "GENERIC_ASSAY",
"generic_assay_type": "MUTATIONAL_SIGNATURE",
"datatype": "LIMIT-VALUE",
"stable_id": "mutational_signature_dbs",
"profile_name": "generic assay test profile DBS",
"profile_description": "test profile for generic assay DBS",
"data_filename": "data_mutational_signatures_counts_DBS.txt",
"generic_entity_meta_properties": "NAME",
"show_profile_in_analysis_tab": "true"
}

meta_mutational_signatures_id_counts ={
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "GENERIC_ASSAY",
"generic_assay_type": "MUTATIONAL_SIGNATURE",
"datatype": "LIMIT-VALUE",
"stable_id": "mutational_signature_id",
"profile_name": "generic assay test profile ID",
"profile_description": "test profile for generic assay ID",
"data_filename": "data_mutational_signatures_counts_ID.txt",
"generic_entity_meta_properties": "NAME",
"show_profile_in_analysis_tab": "true"
}

meta_mutational_signatures_sbs_contribution = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "GENERIC_ASSAY",
"generic_assay_type": "MUTATIONAL_SIGNATURE",
"datatype": "LIMIT-VALUE",
"stable_id": "mutational_signatures_contribution_SBS",
"profile_name": "Mutational signatures contribution SBS",
"profile_description": "Mutational signature contribution",
"data_filename": "data_mutational_signatures_contribution_SBS.txt",
"show_profile_in_analysis_tab": "true",
"generic_entity_meta_properties": "NAME,DESCRIPTION,URL",
"value_sort_order": "DESC",
}

meta_mutational_signatures_dbs_contribution = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "GENERIC_ASSAY",
"generic_assay_type": "MUTATIONAL_SIGNATURE",
"datatype": "LIMIT-VALUE",
"stable_id": "mutational_signatures_contribution_DBS",
"profile_name": "Mutational signatures contribution DBS",
"profile_description": "Mutational signature contribution",
"data_filename": "data_mutational_signatures_contribution_DBS.txt",
"show_profile_in_analysis_tab": "true",
"generic_entity_meta_properties": "NAME,DESCRIPTION,URL",
"value_sort_order": "DESC",
}


meta_mutational_signatures_id_contribution = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "GENERIC_ASSAY",
"generic_assay_type": "MUTATIONAL_SIGNATURE",
"datatype": "LIMIT-VALUE",
"stable_id": "mutational_signatures_contribution_ID",
"profile_name": "Mutational signatures contribution ID",
"profile_description": "Mutational signature contribution",
"data_filename": "data_mutational_signatures_contribution_ID.txt",
"show_profile_in_analysis_tab": "true",
"generic_entity_meta_properties": "NAME,DESCRIPTION,URL",
"value_sort_order": "DESC",
}

meta_mutations_extended = {
"cancer_study_identifier": f"{cancer_study_id}",
'genetic_alteration_type': 'MUTATION_EXTENDED',
'datatype': 'MAF',
'stable_id': 'mutations',
'show_profile_in_analysis_tab': 'true',
'profile_description': 'Mutation data from whole exome sequencing.',
'profile_name': 'Mutations',
'data_filename': 'data_mutations.txt',
'swissprot_identifier': 'name',
'namespaces': 'CUSTOM'
}



if __name__ == "__main__":
   #create_meta_data(meta_cna_discrete, 'synthetic_data/meta_cna_discrete.txt')
   #create_meta_data(meta_cna_log2, 'synthetic_data/meta_cna_log2.txt')
   #create_meta_data(meta_cna_hg19, 'synthetic_data/meta_cna_hg19_seg.txt')
   #create_meta_data(meta_gsva_scores, 'synthetic_data/meta_gsva_scores.txt')
   #create_meta_data(meta_gsva_pvalues, 'synthetic_data/meta_gsva_pvalues.txt')
   #create_meta_data(meta_clinical_patients, 'synthetic_data/meta_clinical_patients.txt')
   #create_meta_data(meta_clinical_samples, 'synthetic_data/meta_clinical_samples.txt')
   #create_meta_data(meta_structural_variants, 'synthetic_data/meta_structural_variants.txt')
   #create_meta_data(meta_methylation_hm27, 'synthetic_data/meta_methylation_hm27.txt')
   #create_meta_data(meta_study, 'synthetic_data/meta_study.txt')
   #create_meta_data(meta_treatment_ic50, 'synthetic_data/meta_treatment_ic50.txt')
   #create_meta_data(meta_expression_continuous, 'synthetic_data/meta_expression_continuous.txt')
   #create_meta_data(meta_mutational_signatures_sbs_counts, 'synthetic_data/meta_mutational_signatures_counts_SBS.txt')
   #create_meta_data(meta_mutational_signatures_dbs_counts, 'synthetic_data/meta_mutational_signatures_counts_DBS.txt')
   #create_meta_data(meta_mutational_signatures_id_counts, 'synthetic_data/meta_mutational_signatures_counts_ID.txt')
   #create_meta_data(meta_mutational_signatures_sbs_contribution,
   #                 'synthetic_data/meta_mutational_signatures_contribution_SBS.txt')
   #create_meta_data(meta_mutational_signatures_dbs_contribution,
   #                 'synthetic_data/meta_mutational_signatures_contribution_DBS.txt')
   #create_meta_data(meta_mutational_signatures_id_contribution,
   #                 'synthetic_data/meta_mutational_signatures_contribution_ID.txt')
   create_meta_data(meta_mutations_extended, 'synthetic_data/meta_mutations.txt')