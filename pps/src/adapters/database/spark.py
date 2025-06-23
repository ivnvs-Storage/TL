from pyspark.sql import SparkSession
from pps.src.config import settings

spark: SparkSession = SparkSession.builder.getOrCreate()

def make_spark_session():
    return SparkSession.builder.appName("TL-Spark").getOrCreate()
