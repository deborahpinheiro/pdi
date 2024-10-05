import pandas as pd
import unicodedata as un
import re
import psutil
import os
from dotenv import load_dotenv

load_dotenv()

reception_path = os.getenv('PATH_TABLE_RECEPTION')

def read_dict_reception(source_id):
    """
    Reads the reception table and returns a dictionary for the given source ID.

    Args:
        source_id (int): The ID of the source for which to retrieve the reception data.

    Returns:
        dict: A dictionary containing the reception data for the specified source ID.
    """

    dict_reception = pd.read_excel(reception_path, engine='openpyxl')
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