from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, StructType, IntegerType, FloatType, TimestampType
from pyspark.sql.functions import *

spark = SparkSession.builder.master("spark://spark-master:7077"
                ).appName('Processed raw data'
                ).getOrCreate()

schema = StructType([
    StructField('ride_id', StringType(), False),
    StructField('rideable_type', StringType(), True),
    StructField('started_at', TimestampType(), False),
    StructField('ended_at', TimestampType(), False),
    StructField('start_station_name', StringType(), True),
    StructField('start_station_id', StringType(), True),
    StructField('end_station_name', StringType(), True),
    StructField('end_station_id', StringType(), True),
    StructField('start_lat', FloatType(), True),
    StructField('start_lng', FloatType(), True),
    StructField('end_lat', FloatType(), True),
    StructField('end_lng', FloatType(), True),
    StructField('member_casual', StringType(), True)
])

def processed_data(file_path):
    df = spark.read.schema(schema).option("header", "true").csv(file_path)
    print(df.count())