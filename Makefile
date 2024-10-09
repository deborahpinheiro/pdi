IMAGE = executar
VENV = pdi_deborah

create_venv:
	python -m venv $(VENV)

activate_env:
	$(VENV)/Scripts/activate

install: 
	"$(VENV)\Scripts\pip" install -r requirements.txt

run: 
	@echo "Running the application..."
	python src/app.py

clean:
	rmdir /s /q $(VENV)

snakeviz:
	snakeviz resultado.prof

docker/build:
	docker build -t $(IMAGE) .

docker/run:
	@docker run -it $(IMAGE) /bin/sh -c "cd src && python app.py"

#all: create_venv activate_env install run clean

all: docker/build docker/run

