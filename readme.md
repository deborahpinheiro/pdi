# Project Pipeline

This project is designed to handle the reception and processing of data from various sources. The pipeline is modular, comprising two main processes: reception (receptor) and loading (loader), orchestrated through app.py. It is also integrated with Apache Airflow for workflow automation.

## Project Structure

- **`src/app.py`**: The main script to execute the reception and loading processes.
- **`src/services/`**: Contains the service modules (`reception.py` and `loader.py`) for data handling.
- **`src/airflow/dags/`**: Contains Airflow DAGs for orchestrating the pipeline.
- **`src/config/tabelas/`**: Stores configuration files such as metadata and source definitions.

## Prerequisites

Make sure you have the following installed on your machine:

1. **Python 3.9 or higher**
2. **Docker** and **Docker Compose**
3. **Make**

## Setup Instructions

### 1. Clone the Repository

To clone the project repository, run the following commands:

```bash
git clone https://github.com/deborahpinheiro/pdi.git
cd pdi
```

### 2. Register New Sources

To add new data sources, you must update the following Excel files located in the `config/tabelas` directory:

- **`tb_source.xlsx`**: Contains the definitions of the sources.
- **`tb_reception.xlsx`**: Contains the configurations related to data reception (e.g., API URLs, methods, parameters).
- **`tb_metadata.xlsx`**: Contains metadata such as column names, data types, and any necessary preprocessing steps.

### 3. Install Required Dependencies

Ensure that all required Python packages are installed. You can easily install them by running the following command using the Makefile:

```python
make install
```

This command will create a virtual environment (if it doesn't exist) and install the necessary packages listed in requirements.txt.


| Package                           | Version   |
|-----------------------------------|-----------|
| `pandas`                          | `2.2.2`   |
| `openpyxl`                        | `3.1.5`   |
| `requests`                        | `2.32.3`  |
| `pyarrow`                         | `17.0.0`  |
| `python-dotenv`                   | `1.0.1`   |
| `snakeviz`                        | `2.2.0`   |
| `memory_profiler`                 | `0.61.0`  |
| `apache-airflow`                  | `2.7.0`   |
| `apache-airflow-providers-docker` | `3.2.0`   |

### 4. Run the Pipeline
#### Running Locally
To run the pipeline locally, use:

```python
make run_local
```

This will execute app.py and perform the following tasks:

Reception: Retrieve data from the sources specified in the tb_reception.xlsx file and save it in the raw data folder.

Loader: Load the raw data, apply transformations according to the metadata in tb_metadata.xlsx, and save the processed data in the work directory.

#### Running with Docker and Airflow
The project supports Apache Airflow for task orchestration. Follow these steps:

1. Build the Docker Image

Run the following command to build the Docker image:
``` python
make run_docker
```

2. Start Airflow

Start the Airflow instance with:
```
make run_airflow
```

3. Access the Airflow Web UI

Open your browser and navigate to:
```
http://localhost:8080
```

4. Enable and Run the DAGs
- **receptor_dag:** Executes the reception process.
- **load_dag:** Executes the loading process.

5. Stop Airflow

To stop the Airflow services, use:
```
make airflow/stop
```

## Environment Variables
Create a .env file with the following variables to set up the project paths:

```
PROJECT_PATH_RAW=/path/to/raw_data
PROJECT_PATH_WORK=/path/to/work_data
PATH_TABLE_METADATA=/path/to/tb_metadata.xlsx
PATH_TABLE_RECEPTION=/path/to/tb_reception.xlsx
```