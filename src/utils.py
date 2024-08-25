import pandas as pd
import unicodedata as un

def read_dict_reception (source_id):
    filepath = r'tabelas/tb_reception.xlsx'
    dict_reception = pd.read_excel(filepath, engine='openpyxl')
    dict_reception = dict_reception[dict_reception['source_id'] == source_id]

    dict_reception = dict_reception.iloc[0]
    dict_reception = dict_reception.to_dict()

    return dict_reception

def standardize_string(value):
    normalized = un.normalize('NFKD', value).encode('ASCII', 'ignore').decode('ASCII')
    return normalized.upper()

def standardize_numbers(value):
    return re.sub(r'\D', '', value)