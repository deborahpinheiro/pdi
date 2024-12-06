from airflow import DAG
from airflow.operators.python import PythonOperator # esse operador chama um codigo python
from datetime import datetime
#from app import ingestion 
from airflow.providers.docker.operators.docker import DockerOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='receptor_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:
    task_ingestion = DockerOperator(
        task_id='ingestion_load',
        image="executar",
        command=["/bin/sh", "-c", "cd src && python app.py receptor 1"],
        auto_remove='force',
        docker_url='unix://var/run/docker.sock'
        
        )
    
    # task_ingestion = PythonOperator(
    #     task_id='run_ingestion',
    #     python_callable=ingestion,  
    #     op_kwargs={'source_id': '1'}, 
    # )
    # task_load = PythonOperator(
    #     task_id='run_load',
    #     python_callable=load,  
    #     op_kwargs={
    #         'source_id': '1',  
    #         'path': '/path/to/file.csv', 
    #     }, 
    # )

    #task_ingestion >> task_load


#como subir a dag num container executando