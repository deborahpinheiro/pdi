VENV = pdi_deborah
IMAGE = imagem_executar

create_venv:
	python -m venv $(VENV)

install: 
	$(VENV)/Scripts/pip install -r requirements.txt

activate_env:
	$(VENV)\Scripts\activate.bat

run:  #verificar como executa o app.py
	@echo "Running the application..."
	src/app.py

clean:
	rmdir /s /q $(VENV)
all: create_env install activate_env run

docker/build:
	docker build -t $(IMAGE) .

docker/run:
	docker run $(IMAGE)