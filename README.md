## PYSPARK BOILERPLATE

## Introduction:
    This project is designed to demonstrate how to build and deploy an ETL pipeline on Databricks using Python. The pipeline reads data from Azure Data Lake Storage (ADLS), performs some transformations using PySpark, and then writes the transformed data back to ADLS.

## Project Structure:
The project has the following directory structure:

```
└───etl_pipeline
    │   __init__.py
    │
    ├───config
    │       adls_config.json
    │       spark_config.json
    │
    ├───jobs
    │   │   etl_job.py
    │   │   transform.py
    │   │   __init__.py
    │
    ├───schema
    │       __init__.py
    │
    └───tests
            __init__.py

```
1. etl_pipeline: This is the main directory that contains the pipeline code.
2. config: This directory contains the configuration files for the pipeline.
3. jobs: This directory contains the ETL job code that performs the data transformation.
4. schema: This directory contains the schema for the data to be processed.
5. tests: This directory contains the unit tests for the ETL job.

## Setting Up the Project:

    To use this project, you will need to follow the steps below:

    1. Clone the project from GitHub to your Databricks from REPOS in Databricks UI.
    2. Set the configurations for ADLS and Spark in their respective config files.
    3. Connect the workflow task to jobs/etl_jobs.py.


## Configuring the Project:
Before running the ETL job, you will need to configure the project by setting the necessary parameters in the configuration files.

* adls_config.json: This file contains the configuration parameters for connecting to Azure Data Lake Storage. You will need to set the following parameters:

    * STORAGE_URL: The URL of the storage account as 
        ```
            "STORAGE_URL":"fs.azure.account.key.boilerplatestorageacc.dfs.core.windows.net"
        ```
    * CONTAINER: The path of the container as 
        ```
            "CONTAINER":"abfss://boilerplate@boilerplatestorageacc.dfs.core.windows.net"
        ```
* spark_config.json: This file contains the configuration parameters for spark. You will need to set the following parameters:
    * SCOPE_NAME : Name of the scope that you created for the key
        ```
            "SCOPE_NAME":"boilerplate"
        ```
    * SCOPE_KEY : Name of the key
        ```
            "SCOPE_KEY":"boilerplate-storage-key"
        ```

* etl_job.py: This file contains the PySpark code for the ETL job. You will need to set the following parameters:

    INPUT_FILENAME: The name of the input file to read from ADLS.
    OUTPUT_FILENAME: The name of the output file to write to ADLS.