from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import app 

def run_receptor():
    app.receptor(source_id=1)

with DAG(
    dag_id='receptor_dag_biblia',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    receptor_task = PythonOperator(
        task_id='receptor_task',
        python_callable=run_receptor
    )