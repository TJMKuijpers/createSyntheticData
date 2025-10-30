import polars as pl
from polars import DataFrame
import numpy as np
import random

def get_patient_or_sample_identifiers(input_file,sep,select_column,skip_lines):
    df = pl.read_csv(input_file,separator=sep,skip_lines=skip_lines).select(select_column)
    return df

def combine_dataframes_horizontal(*dataframes: DataFrame) -> DataFrame:
    if not dataframes:
        raise ValueError("At least one DataFrame must be provided.")
    new_df = pl.concat(dataframes, how='horizontal')
    return new_df

def create_categorical_values(number_of_replicates,option_list,column_name):
    # Randomize categorical options
    values =  [random.choice(option_list) for i in range(0,number_of_replicates)]
    return pl.DataFrame({column_name:values})

def create_numerical_values(number_of_replicates,min_value,max_value,number_of_decimals,column_name):
    values = [round(random.uniform(min_value, max_value), number_of_decimals)  for i in range(number_of_replicates)]
    return pl.DataFrame({column_name:values})

def read_gene_json(input_json,entrezGeneColumn,HugoGeneColumn):
    df = pl.read_json(input_json)
    return df.select([entrezGeneColumn,HugoGeneColumn])

def replace_sample_ids(df, sample_ids, sample_col="SAMPLE_ID"):
	n_samples = len(sample_ids)
	n_rows = df.height
	df = df.with_columns([
		pl.Series(sample_col, [sample_ids[i % n_samples] for i in range(n_rows)])
	])
	return df

def duplicate_rows(df, fraction):
    n_duplicate = int(fraction * df.height)
    if n_duplicate > 0:
        duplicate_rows = df.sample(n_duplicate, with_replacement=True)
        df = pl.concat([df, duplicate_rows])
        df = df.sample(df.height, shuffle=True)
    return df

def add_custom_namespace_cols(df):
    custom_name_col = [random.choice(["custom_annotation_1", "custom_annotation_2", ""]) for _ in range(df.height)]
    custom_type_col = [random.choice(["custom_type_1", "custom_type_2", ""]) for _ in range(df.height)]
    df = df.with_columns([
        pl.Series("CUSTOM.name", custom_name_col),
        pl.Series("CUSTOM.type", custom_type_col)
    ])
    return df

def create_expression_matrix(column_list,column_name,min_value,max_value,number_of_entries,profile):
    names = column_list[column_name].to_list()
    data = {}
    if profile.upper() == 'EXPR' or profile.upper() == 'COUNT':
        for name in names:
            data[name] = np.random.randint(
                low=min_value,
                high=max_value,
                size=number_of_entries
            )
    elif profile.upper() == 'RPPA' or profile.upper() == 'PVALUE'  or profile.upper() == 'SCORE' or profile.upper() == 'CONTRIBUTION':
        for name in names:
            data[name] = np.random.uniform(
                low=min_value,
                high=max_value,
                size=number_of_entries
            )
    else:
        raise ValueError(F"Profile '{profile}' is not implemented yet")
    df = pl.DataFrame(data)
    return df


def create_categorical_matrix(column_list,column_name,categories,number_of_entries):
    names = column_list[column_name].to_list()
    data = {}
    for name in names:
        data[name] = np.random.choice(
             a=categories,
             size=number_of_entries)
    df = pl.DataFrame(data)
    return df


def create_meta_data(metadata_dict,filename):
    file_content = []
    for key, value in metadata_dict.items():
        file_content.append(f"{key}: {value}")
    file_content_string =  "\n".join(file_content)
    try:
        with open(filename, 'w') as f:
            f.write(file_content_string)
    except Exception as e:
        print("Could not write metadata")
