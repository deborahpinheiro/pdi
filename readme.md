# Project Pipeline

This project is designed to handle the reception and processing of data from various sources. The pipeline is divided into two main modules: reception and loader, both controlled by the main script app.py. Below you will find instructions on how to set up and use this pipeline efficiently on any machine.

## Setup Instructions

### 1. Register New Sources

To add new data sources, you must update the following Excel files located in the `config/tabelas` directory:

- **`tb_source.xlsx`**: Contains the definitions of the sources.
- **`tb_reception.xlsx`**: Contains the configurations related to data reception (e.g., API URLs, methods, parameters).
- **`tb_metadata.xlsx`**: Contains metadata such as column names, data types, and any necessary preprocessing steps.

### 2. Configure Project Path

After creating a project directory on your local machine, you need to set the path in the env.py file located in the assets/ directory. Update the PROJECT_PATH variable with the path to your project directory. This will ensure that the pipeline stores raw and processed data correctly.

```python
# assets/env.py
import os

PROJECT_PATH = os.getenv("PROJECT_PATH", "C:/path/to/your/project")
```

### 3. Install Required Dependencies

Ensure that all required Python packages are installed. You can easily install them by running the following command using the Makefile:

```python
make install
```

This command will create a virtual environment (if it doesn't exist) and install the necessary packages listed in requirements.txt.

### 4. Run the Pipeline
Once everything is configured and the dependencies are installed, you can run the pipeline by executing the following command:

```python
make run
```

This command will execute the app.py script, which will perform the following tasks:

Reception: Retrieve data from the sources specified in the tb_reception.xlsx file and save it in the raw data folder.

Loader: Load the raw data, apply transformations according to the metadata in tb_metadata.xlsx, and save the processed data in the work directory.

### Additional Information
Utils Module: The utils.py file contains helper functions used across the pipeline, such as data standardization functions.
Modularization: The pipeline is divided into modular components (reception.py and loader.py) to maintain clarity and reusability.

### Running on Different Machines
To ensure that the pipeline runs smoothly on different machines:

1. Make sure to have Python and Make installed.
2. Clone the repository to your local machine.
3. Set the PROJECT_PATH in the env.py file to match your local directory structure.
4. Run make install to set up the environment.
5. Execute make run to start the pipeline.

By following these steps, you can effectively run the project pipeline on any machine without issues. If you encounter any problems, feel free to reach out for assistance.