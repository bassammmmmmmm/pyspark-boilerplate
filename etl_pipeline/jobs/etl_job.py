df_pyspark = spark.read.option("header", "true").csv(
    "../data/input/titanic.csv", inferSchema=True
)
df_pyspark.show(10)
type(df_pyspark)
df_pyspark.printSchema()
df_pyspark.select("Name").show()
df_pyspark_output = df_pyspark.filter("age>20")
df_pyspark_output.describe().show()
df_pyspark_output.write.csv("../data/output/output.csv")
