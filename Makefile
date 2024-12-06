IMAGE = executar
AIRFLOW_HOME = ./src/airflow
AIRFLOW_WEBSERVER=airflow-webserver


# Local Execution
create_venv:
	python -m venv venv

install:
	venv/Scripts/pip install -r requirements.txt

run_app:
	venv/Scripts/python src/app.py

clean_venv:
	rm -rf venv

# Docker Execution
docker/build:
	docker build -t $(IMAGE) .

docker/run:
	docker run -it $(IMAGE) /bin/sh -c "cd src && python app.py"

# Airflow with Docker Compose

airflow_start:
	docker-compose -f docker-compose-airflow.yml up -d

delete_admin:
	docker exec -it $(AIRFLOW_WEBSERVER) airflow users delete --username admin

create_admin:
	docker exec -it $(AIRFLOW_WEBSERVER) airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

airflow_stop:
	docker-compose -f docker-compose-airflow.yml down

airflow_logs:
	docker-compose -f docker-compose-airflow.yml logs

airflow_reset:
	docker-compose -f docker-compose-airflow.yml down -v
	docker-compose -f docker-compose-airflow.yml up -d

#--------------------------------------------------
run_local:
	make create_venv install run-app clean_venv

run_docker:
	make docker/build docker/run

run_airflow:
	make airflow_start delete_admin create_admin

run_reset_airflow:
	make airflow_reset delete_admin create_admin


