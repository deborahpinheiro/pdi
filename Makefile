IMAGE = executar

create_venv:
	python -m venv $(VENV)

install: 
	$(VENV)/Scripts/pip install -r requirements.txt

activate_env:
	$(VENV)\Scripts\activate

run: 
	@echo "Running the application..."
	python src/app.py

clean:
	rm -rf /s /q $(VENV)

docker/build:
	docker build -t $(IMAGE) .

docker/run:
	@docker run -it $(IMAGE) /bin/sh -c "cd src && python app.py"

all: docker/build docker/run

#create_venv install activate_env run