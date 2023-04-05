from pyspark.sql import DataFrame


def transform(df: DataFrame) -> DataFrame:
    df = df.filter("age>20")
    return df
