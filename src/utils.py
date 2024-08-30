import pandas as pd
import unicodedata as un
import psutil

def read_dict_reception (source_id):
    filepath = r'tabelas/tb_reception.xlsx'
    dict_reception = pd.read_excel(filepath, engine='openpyxl')
    dict_reception = dict_reception[dict_reception['source_id'] == source_id]

    dict_reception = dict_reception.iloc[0]
    dict_reception = dict_reception.to_dict()

    return dict_reception

def standardize_string(value):
    normalized = un.normalize('NFKD', value).encode('ASCII', 'ignore').decode('ASCII')
    return normalized.upper()

def standardize_numbers(value):
    return re.sub(r'\D', '', value)

def report_resource_usage():
    # Uso de CPU
    cpu_usage = psutil.cpu_percent(interval=1)  # Intervalo para calcular a média
    
    # Uso de Memória
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    memory_used = memory_info.used / (1024 ** 2)  # Converte de bytes para MB
    memory_total = memory_info.total / (1024 ** 2)  # Converte de bytes para MB

    # Relatório
    print("=== Resource Usage Report ===")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Memory Used: {memory_used:.2f} MB")
    print(f"Memory Total: {memory_total:.2f} MB")
    print("=============================")