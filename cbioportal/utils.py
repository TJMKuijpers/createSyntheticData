import polars as pl
import random

def get_patient_or_sample_identifiers(input_file,sep,select_column):
    df = pl.read_csv(input_file,separator=sep).select(select_column)
    return df

def combine_dataframes_horizontal(df1,df2):
    new_df  = pl.concat([df1, df2],how='horizontal')
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
