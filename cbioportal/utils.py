import polars as pl

def get_patient_identifiers(input_file,sep):
    df = pl.read_csv(input_file,separator=sep).select('PATIENT_ID')
    return df

def get_patient_ids_from_file(input_file,sep):
    data = pl.read_csv(input_file,seperator=sep)
    return data['PATIENT_ID']

def combine_dataframes_horizontal(df1,df2):
    new_df  = pl.concat([df1, df2],how='horizontal')
    return new_df