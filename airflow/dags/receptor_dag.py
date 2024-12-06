from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from app import ingestion 

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='receptor_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:
    task_ingest = PythonOperator(
        task_id='run_ingestion',
        python_callable=ingestion,  
        op_kwargs={'source_id': '1'}, 
    )

    task_ingest
