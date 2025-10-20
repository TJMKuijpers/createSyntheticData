import polars as pl
import numpy as np
import math
import polars.selectors as cs

from formulaic.utils.stateful_transforms import sanitize_variable_name

from utils import get_patient_or_sample_identifiers, combine_dataframes_horizontal,read_gene_json

# Columns in CNA discrete
# Hugo_Symbol
# Entrez_Gene_id
# SAmple_id
# Value
#cbp

def create_expression_matrix(column_list,number_of_entries):
    names = column_list["SAMPLE_ID"].to_list()
    data = {
        name: np.random.choice([-2,-1,0,1,2], size=number_of_entries)
        for name in names
    }
    df = pl.DataFrame(data)
    return df

def create_log2_matrix(column_list,number_of_entries):
    sample_ids= column_list["SAMPLE_ID"].to_list()
    data = {
        name: np.log2(np.random.randint(low=-10, high=10, size=number_of_entries))
        for name in sample_ids
    }
    df = pl.DataFrame(data)
    return df

def create_cna_discrete(genes,identifiers,number_of_entries):
    values = np.random.choice([-2,-1,0,1,2], size=300000)
    dataframes=[genes]*300
    gene_for_samples= pl.concat(dataframes)
    df=pl.DataFrame({'HUGO_SYMBOL':gene_for_samples['hugoGeneSymbol'],'Entrez_Gene_Id':gene_for_samples['entrezGeneId'],'Sample_Id':identifiers,'Value':values})
    return df

def create_cna_hg19(df,identifiers):
    df.drop('ID')
    dataframes = [df]*2
    cna_for_samples = pl.concat(dataframes)
    identifiers_subset=identifiers[0:234462]
    df = pl.DataFrame({'ID':identifiers_subset,'chrom':cna_for_samples['chrom'],'loc.start':cna_for_samples['chrom'],'loc.end':cna_for_samples['loc.end'],'num.mark':cna_for_samples['num.mark'],'seg.mean':cna_for_samples['seg.mean']})
    return df


if __name__ == "__main__":
    sample_identifiers = get_patient_or_sample_identifiers('data_clinical_sample.txt', sep='\t', select_column='SAMPLE_ID')
    gene_identifiers = read_gene_json('gene_identifiers.json',"entrezGeneId","hugoGeneSymbol")
    gene_identifiers_subset = gene_identifiers[1500:2500, :]
    number_of_genes = gene_identifiers_subset.shape[0]
    cna_df = create_expression_matrix(sample_identifiers, number_of_genes)
    gene_cna_df = combine_dataframes_horizontal(pl.DataFrame(gene_identifiers_subset['hugoGeneSymbol']), cna_df)
    #gene_cna_df.write_csv('data_cna.txt', separator='\t')
    #cna_log2_values = create_log2_matrix(sample_identifiers, number_of_genes)
    #cna_log2_values.with_columns((~cs.string()).replace([float("inf"), -float("inf")], 'NaN'))
    #gene_cna_log2_df = combine_dataframes_horizontal(pl.DataFrame(gene_identifiers_subset['hugoGeneSymbol']), cna_log2_values)
    #gene_cna_df.write_csv('data_cna_log2.txt', separator='\t')
    #cna_discrete=create_cna_discrete(gene_identifiers_subset,sample_identifiers,number_of_genes)
    #cna_discrete.write_csv('data_cna_discrete.txt', separator='\t')
    cna_hg19_data = pl.read_csv('/home/tkuijpers/git/sourceCodecBioPortal/datahub/public/coad_silu_2022/data_cna_hg19.seg',separator='\t',infer_schema_length=10000)
    cna_hg19 = create_cna_hg19(cna_hg19_data,sample_identifiers)
    cna_hg19.write_csv('data_cna_hg19.seg', separator='\t')