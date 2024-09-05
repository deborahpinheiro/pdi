VENV = pdi_deborah

create_venv:
	python -m venv $(VENV)

install: create_venv
	$(VENV)/Scripts/pip install -r requirements.txt

run: install
	@echo "Running the application..."
	$(VENV)/Scripts/python -m src.app

clean:
	rmdir /s /q $(VENV)
all: run
