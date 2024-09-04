# Nome do ambiente virtual
VENV = pdi_deborah

# Comando para criar o ambiente virtual
create_venv:
	python -m venv $(VENV)

# Comando para instalar as dependências
install: create_venv
	$(VENV)/Scripts/activate && pip install -r requirements.txt

# Comando para executar o pipeline
run: install
	$(VENV)/Scripts/activate && python -m src.app

# Comando para limpar o ambiente (opcional)
clean:
	rm -rf $(VENV)

# Comando para rodar todos os passos
all: run
