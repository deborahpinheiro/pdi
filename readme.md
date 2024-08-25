# Project Pipeline

This project is designed to handle the reception and processing of data from various sources. The pipeline is divided into two main modules: `reception` and `loader`, both controlled by the main script `app.py`. Below you will find instructions on how to set up and use this pipeline.

## Setup Instructions

### 1. Register New Sources

To add new data sources, you must update the following Excel files located in the `tabelas/` directory:

- **`tb_source.xlsx`**: Contains the definitions of the sources.
- **`tb_reception.xlsx`**: Contains the configurations related to data reception (e.g., API URLs, methods, parameters).
- **`tb_metadata.xlsx`**: Contains metadata such as column names, data types, and any necessary preprocessing steps.

### 2. Configure Project Path

After creating a project directory on your local machine, you need to set the path in the `config_project.py` file. Update the `project_path` variable with the path to your project directory. This will ensure that the pipeline stores raw and processed data correctly.

```python
# config_project.py
project_path = "/path/to/your/project"
```

### 3. Install Required Dependencies

Ensure that all required Python packages are installed by running the following command:

```python
pip install -r requirements.txt
```

### 4. Run the Pipeline
Once everything is configured, you can run the pipeline by executing the app.py script.

src/app.py

This script will:

Reception: Retrieve data from the sources specified in the tb_reception.xlsx file and save it in the raw data folder.

Loader: Load the raw data, apply transformations according to the metadata in tb_metadata.xlsx, and save the processed data in the work directory.

### Additional Information
Utils Module: The utils.py file contains helper functions used across the pipeline, such as data standardization functions.
Modularization: The pipeline is divided into modular components (reception.py and loader.py) to maintain clarity and reusability.