from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append('/opt/airflow/dags')  
from app import load

def run_load(**context):
    # Recupera o valor do path do XCom
    path = context['ti'].xcom_pull(key='path', task_ids='run_receptor')
    if not path:
        raise ValueError("No path found in XCom. Ensure the receptor DAG ran successfully.")
    load(path, 1)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'load_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:
    load_task = PythonOperator(
        task_id='run_load',
        python_callable=run_load,
        provide_context=True,
    )
