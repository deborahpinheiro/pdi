import services.reception as reception
import services.loader as loader
import utils
from timeit import timeit
from io import StringIO
import logging 
import stats_utils as su

def receptor(source_id):
    
    try:
        logging.info("Iniciando o processo de Recepção...")
        df_raw = reception.process_source(source_id = source_id)
        
        logging.info(f"Processo de Recepção executado com sucesso!")
        return df_raw
    
    except Exception as e:
        logging.error("Erro ao executar: ", exc_info=True)

def load(df,source_id):
    try:
        logging.info("Iniciando o processo de Carga e tratamento.")
        loader.process_data(df=df, source_id=source_id)
    
    except Exception as e:
        logging.error("Erro ao executar:", exc_info=True)
       

if __name__ == "__main__":
    
    df = receptor(1)
    
    load(df, 1)