import json
from typing import Dict


def load_config_file(file_name: str) -> Dict:
    """
    Reads the configs/config.json file and parse as a dictionary

    :param file_name: name of the config file
    :return: config dictionary
    """
    try:
        with open(f"{file_name}", "r") as f:
            conf: Dict = json.load(f)
        return conf

    except FileNotFoundError:
        raise FileNotFoundError(f"{file_name} Not found")


def set_spark_conf(scope_name: str, scope_key: str, storage_url: str):
    # SCOPE = dbutils.secrets.get(scope="boilerplate", key="boilerplate-storage-key")
    # STORAGE = "fs.azure.account.key.boilerplatestorageacc.dfs.core.windows.net"
    SCOPE = dbutils.secrets.get(scope=scope_name, key=scope_key)
    STORAGE = storage_url
    spark.conf.set(STORAGE, SCOPE)


def extract(container, filename):
    df_pyspark = spark.read.csv(container + filename, header=True, inferSchema=True)
    return df_pyspark


def transform(df):
    df = df.filter("age>20")
    return df


def load(df, container):
    df.write.format("csv").save(container + "/output/", mode="overwrite")


def run():

    ADLS_CONF, SPARK_CONF = load_config_file(
        "config/adls_config.json"
    ), load_config_file("config/spark_config.json")

    set_spark_conf(
        SPARK_CONF["SCOPE_NAME"], SPARK_CONF["SCOPE_KEY"], ADLS_CONF["STORAGE_URL"]
    )

    FILENAME = "/input/titanic.csv"

    df = extract(ADLS_CONF["CONTAINER"], FILENAME)
    df = transform(df)
    load(df)


if __name__ == "__main__":
    run()
