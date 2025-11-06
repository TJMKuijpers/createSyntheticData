import polars as pl
import os
from utils import create_meta_data

def create_case_list(cancer_study_id,stable_id,case_list_name,case_list_description,case_list_ids):
    case_list_temp = {
        "cancer_study_identifier": f"{cancer_study_id}",
        "stable_id": f"{stable_id}",
        "case_list_name": f"{case_list_name}",
        "case_list_description":f"{case_list_description}",
        "case_list_ids":f"{case_list_ids}",
    }
    return case_list_temp


def write_case_list(path,case_list):
    file_content = []
    for key, value in case_list.items():
        file_content.append(f"{key}: {value}")
    file_content_string =  "\n".join(file_content)
    try:
        with open(path, 'w') as f:
            f.write(file_content_string)
    except Exception as e:
        print(e)
        print("Could not write metadata")


if __name__ == "__main__":
    cancer_study_id = "fake_clickhouse_100k"
    stable_id = "fake_clickhouse_100k_cna"
    case_list_name = 'Samples profiled for CNA'
    case_list_description = "This is he case list that contains all samples with CNA data"
    case_list_ids=pl.scan_csv(os.path.join(os.getcwd()+'/synthetic_data/data_cna_discrete.txt'),separator='\t',n_rows=3).collect().columns
    case_list_ids.remove('Hugo_Symbol')
    case_list_ids='\t'.join(case_list_ids)
    cna_case_lists=create_case_list(cancer_study_id,stable_id,case_list_name,case_list_description,case_list_ids)
    write_case_list('synthetic_data/case_lists/cna_case_list.txt', cna_case_lists)


    mutations = pl.scan_csv(os.path.join(os.getcwd()+'/synthetic_data/data_mutations.txt'),separator='\t').select(pl.col('Tumor_Sample_Barcode')).collect()
    mutations = "\t".join(mutations['Tumor_Sample_Barcode'].unique().to_list())
    mutation_case_list=create_case_list(cancer_study_id,'fake_clickhouse_100k_sequenced','Samples with mutation data','Samples with  mutation data',mutations)
    write_case_list('synthetic_data/case_lists/mutation_case_list.txt', mutation_case_list)