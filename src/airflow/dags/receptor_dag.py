from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import json
sys.path.append('/opt/airflow/dags')  # Ajuste o caminho conforme necessário
from app import receptor

def run_receptor(**context):
    # Executa a função receptor e salva o resultado no XCom
    result = receptor(1)
    context['ti'].xcom_push(key='path', value=result.get('path'))

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'receptor_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:
    receptor_task = PythonOperator(
        task_id='run_receptor',
        python_callable=run_receptor,
        provide_context=True,
    )
