# Create meta data
metadata_cna_discrete = {
    "cancer_study_identifier": f"{cancer_study_id}",
     "genetic_alteration_type": "COPY_NUMBER_ALTERATION",
     "datatype": "DISCRETE_LONG",
     "stable_id": "gistic",
     "show_profile_in_analysis_tab": "true",
     "profile_description": "Putative copy-number from GISTIC 2.0. Values: -2 = homozygous deletion; -1 = hemizygous deletion; 0 = neutral / no change; 1 = gain; 2 = high level amplification.",
     "profile_name": "Putative copy-number alterations from GISTIC",
     "data_filename": "data_cna_discrete.txt",
     "namespaces": "MyNamespace,MyNamespace2"
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
