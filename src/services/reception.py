import requests
import pandas as pd
import json
import os
import datetime
import utils as ut
from dotenv import load_dotenv
import logging as log

load_dotenv()

raw_path = os.getenv('PROJECT_PATH_RAW')

def process_source(source_id):
    """
   Processes the source data for a given source ID by fetching data from an API.
    If it's a two-step process, fetches an auth token via POST and then uses it in a GET request.

    Args:
        source_id (int): The ID of the source to process.

    Returns:
        pd.DataFrame: A DataFrame containing the fetched data from the API.
    """
    log.info("Iniciando o processo de Recepção da origem.")
    
    today_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    dict_reception = ut.read_dict_reception(source_id)
    source = dict_reception.get('source')
    subsource = dict_reception.get('subsource')
    
    log.info(f"Origem: {source}/{subsource}")

    if dict_reception.get('ingestion_type').lower() == 'api' and dict_reception.get('method_api_1').lower() == 'post':
        
        url_post = dict_reception.get('url_api_1')
        headers_post = dict_reception.get('headers_api_1')
        params_post = dict_reception.get('params_api_1')
        data_post = dict_reception.get('data_api_1')

        params_post = json.loads(params_post) if isinstance(params_post, str) and params_post != '' else None
        data_post = json.loads(data_post) if isinstance(data_post, str) and data_post != '' else {}
        headers_post = json.loads(headers_post) if isinstance(headers_post, str) and headers_post != '{}' else {"Content-Type": "application/json"}

        response_post = requests.post(url_post, headers=headers_post, data=json.dumps(data_post))
        
        if response_post.status_code == 200:
            token = response_post.json().get('access_token')
        else:
            raise Exception(f"Failed to retrieve token: {response_post.text}")
        
        url_get = dict_reception.get('url_api_2')
        headers_get = {
        "Authorization": f"Bearer {token}"
        }
         
        params_get = dict_reception.get('params_api_2')
        params_get = json.loads(params_get) if isinstance(params_get, str) and params_get != '' else None

        response_get = requests.get(url_get, headers=headers_get, params=params_get)
        
        if response_get.status_code == 200:
        
            response_json = response_get.json()

            df = pd.json_normalize(response_json['data']) 
            df = ut.recursive_normalize(df)
        else:
            raise Exception(f"Erro na requisição GET: {response_get.status_code} - {response_get.text}")

        df['load_date'] = today_date
        
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        hour = datetime.datetime.now().strftime('%H_%M_%S')
        
        path = f"{raw_path}/{source}/{subsource}/{date}"
        os.makedirs(path, exist_ok=True)
        df.to_parquet(f"{path}/{hour}.parquet")

        return df
        
    elif dict_reception.get('ingestion_type').lower() == 'api' and dict_reception.get('method_api_1').lower() == 'get':

        method = dict_reception.get('method_api_1', 'get').lower()
        url = dict_reception.get('url_api_1')
        headers = dict_reception.get('headers_api_1')
        params = dict_reception.get('params_api_1')
        data = dict_reception.get('data_api_1')

        headers = json.loads(headers) if isinstance(headers, str) and headers != '{}' else None
        params = json.loads(params) if isinstance(params, str) and params != '' else None
        data = json.loads(data) if isinstance(data, str) and data != '' else None

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
        
        path = f"{raw_path}/{source}/{subsource}/{date}"
        os.makedirs(path, exist_ok=True)
        df.to_parquet(f"{path}/{hour}.parquet")

        return df
