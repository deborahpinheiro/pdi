import services.reception as reception
import services.loader as loader
import utils
from timeit import timeit
from io import StringIO
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def receptor(source_id):

    try:

        result_dict = reception.process_source(source_id = source_id)

        logging.info(result_dict)   
        logging.info(f"Processo de Recepção executado com sucesso!")

        return result_dict
    
    except Exception as e:

        logging.error("Erro ao executar: ", exc_info=True)
 
def load(path,source_id):

    try:

        logging.info("Iniciando o processo de Carga e tratamento.")
        loader.process_data(path=path, source_id=source_id)

    except Exception as e:

        logging.error("Erro ao executar:", exc_info=True)

if __name__ == "__main__":

    result = receptor(1)
    path = result.get("path")

    load(path, 1) #teste

 