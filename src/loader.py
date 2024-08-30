import pandas as pd
import os
import config_project as cp
import utils as ut

def process_data(df_raw, source_id):
    dict_reception = ut.read_dict_reception(source_id)
    source = dict_reception.get('source')
    subsource = dict_reception.get('subsource')

    metadata_df = pd.read_excel('tabelas/tb_metadata.xlsx')

    rename_dict = dict(zip(metadata_df['column_name'], metadata_df['renamed_column']))
    df_raw = df_raw.rename(columns=rename_dict)

    prep_type_dict = dict(zip(metadata_df['renamed_column'], metadata_df['prep_type']))
    dtype_dict = dict(zip(metadata_df['renamed_column'], metadata_df['data_type']))
    
    for col, dtype in dtype_dict.items():
        df_raw[col] = df_raw[col].astype(str).apply(str.strip)
        
        if prep_type_dict.get(col) == 'standardize_string':
            df_raw[col + '_formatted'] = df_raw[col].apply(ut.standardize_string)
        elif prep_type_dict.get(col) == 'standardize_numbers':
            df_raw[col + '_formatted'] = df_raw[col].apply(ut.standardize_numbers)

        if dtype.lower() == "int":
            df_raw[col] = df_raw[col].astype('int64')
        elif dtype.lower() in ['double', 'float', 'numeric', 'decimal']:
            df_raw[col] = df_raw[col].astype('float')
        elif dtype.lower() in ['datetime','timestamp']:
            df_raw[col] = pd.to_datetime(df_raw[col])
        elif dtype.lower() in ['bool', 'boolean', 'booleano']:
            df_raw[col] = df_raw[col].map({'sim': True, 'não': False, 'true': True, 'false': False})
            df_raw[col] = df_raw[col].astype(bool)

    key_columns = metadata_df.loc[metadata_df['key'] == True, 'renamed_column'].tolist()
    df_raw = df_raw[~df_raw.duplicated(subset=key_columns, keep=False)]

    os.makedirs(f"{cp.project_path_work}/{source}/{subsource}", exist_ok=True)
    df_raw.to_parquet(f"{cp.project_path_work}/{source}/{subsource}/{subsource}.parquet")

