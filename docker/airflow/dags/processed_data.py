from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, StructType, IntegerType, FloatType, TimestampType
from pyspark.sql.functions import *
from pyspark.conf import SparkConf
# import findspark

def procees_data(source, destination):
    conf = SparkConf().setAppName('Processed raw data'
                    ).setMaster("spark://spark-master:7077")
                    # ).set('spark.driver.port','35155'
                    # ).set('spark.driver.host', 'localhost')
                    # ).set('spark.driver.bindAddress','')

    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    spark.sparkContext.setLogLevel('WARN')

    # name_file = '/opt/file_storage/202102-divvy-tripdata.csv'
    spark
    df = spark.read.csv(source)
    records_count = df.count()
    print(records_count)
    with open(destination + '.txt', 'w') as f:
        f.write(str(records_count))
    


if __name__ == "__main__":
    # findspark.init()
    # print("xxxxxxxxxxxxx")
    # print(procees_data('/opt/file_storage/202301-divvy-tripdata.csv'))
    # print("yyyyyyyyyyyyy")
    pass