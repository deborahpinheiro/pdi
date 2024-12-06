from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from app import load

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='load_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:
    task_load = PythonOperator(
        task_id='run_load',
        python_callable=load,  
        op_kwargs={
            'source_id': '1',  
            'path': '/path/to/file.csv', 
        },
    )

    task_load
