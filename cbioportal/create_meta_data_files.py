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
"data_filename": "data_clinical_patients.txt"
}

meta_clinical_samples = {
"cancer_study_identifier": f"{cancer_study_id}",
"genetic_alteration_type": "CLINICAL",
"datatype": "SAMPLE_ATTRIBUTES",
"data_filename": "data_clinical_samples.txt"
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
"gene_panel": f"{gene_panel}",
"namespaces": "StructVarNs,StructVarNs2"
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