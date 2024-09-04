import os

PROJECT_PATH = os.getenv("PROJECT_PATH", "C:/Users/EFHQC/OneDrive - Bayer/Documentos/PDI_PROJECT")

PROJECT_PATH_RAW = f"{PROJECT_PATH}/RAW"
PROJECT_PATH_WORK = f"{PROJECT_PATH}/WORK"

PATH_TABLE_METADATA = f"config/tabelas/tb_metadata.xlsx"
PATH_TABLE_RECEPTION = f"config/tabelas/tb_reception.xlsx"