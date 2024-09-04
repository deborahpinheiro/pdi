import requests
import pandas as pd
import json
import os
import datetime
import utils as ut
import env


def process_source(source_id):
    """
    Processes the source data for a given source ID by fetching data from an API.

    Args:
        source_id (int): The ID of the source to process.

    Returns:
        pd.DataFrame: A DataFrame containing the fetched data from the API.
    """
    today_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    dict_reception = ut.read_dict_reception(source_id)
    source = dict_reception.get('source')
    subsource = dict_reception.get('subsource')

    if dict_reception.get('ingestion_type').lower() == 'api':
        url = dict_reception.get('url_api_1')
        headers = dict_reception.get('headers_api_1')
        params = dict_reception.get('params_api_1')
        data = dict_reception.get('data_api_1')

        headers = json.loads(headers) if isinstance(headers, str) and headers != '{}' else None
        params = json.loads(params) if isinstance(params, str) and params != '' else None
        data = json.loads(data) if isinstance(data, str) and data != '' else None

        method = dict_reception.get('method_api_1', 'get').lower()

        if method == 'get':
            response = requests.get(url, headers=headers, params=params)
        elif method == 'post':
            response = requests.post(url, headers=headers, params=params, data=data)
        else:
            raise ValueError(f'Método {method} não suportado.')

        df = pd.DataFrame(response.json()) 
        df['load_date'] = today_date
        
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        hour = datetime.datetime.now().strftime('%H_%M_%S')
        
        path = f"{env.PROJECT_PATH_RAW}/{source}/{subsource}/{date}"
        os.makedirs(path, exist_ok=True)
        df.to_parquet(f"{path}/{hour}.parquet")

        return df
