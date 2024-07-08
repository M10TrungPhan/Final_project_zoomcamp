from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, StructType, IntegerType, FloatType, TimestampType
from pyspark.sql.functions import *

spark = SparkSession.builder.master("spark://"
                ).appName('Processed raw data'
                ).getOrCreate()