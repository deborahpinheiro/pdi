import pandas as pd
import unicodedata as un
import re
import psutil
import env as env

def read_dict_reception(source_id):
    """
    Reads the reception table and returns a dictionary for the given source ID.

    Args:
        source_id (int): The ID of the source for which to retrieve the reception data.

    Returns:
        dict: A dictionary containing the reception data for the specified source ID.
    """
    filepath = env.PATH_TABLE_RECEPTION

    dict_reception = pd.read_excel(filepath, engine='openpyxl')
    dict_reception = dict_reception[dict_reception['source_id'] == source_id]

    dict_reception = dict_reception.iloc[0]
    dict_reception = dict_reception.to_dict()

    return dict_reception

def standardize_string(value):
    """
    Standardizes a string by normalizing it and converting it to uppercase.

    Args:
        value (str): The string to standardize.

    Returns:
        str: The standardized string in uppercase.
    """
    normalized = un.normalize('NFKD', value).encode('ASCII', 'ignore').decode('ASCII')
    return normalized.upper()

def standardize_numbers(value):
    """
    Standardizes a number by removing non-digit characters.

    Args:
        value (str): The string containing the number to standardize.

    Returns:
        str: The standardized number as a string, containing only digits.
    """
    return re.sub(r'\D', '', value)

def report_resource_usage():
    """
    Reports the current CPU and memory usage statistics.
    Prints the CPU usage percentage and memory usage details.
    """
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
