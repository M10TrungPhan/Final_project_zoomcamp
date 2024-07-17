from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
from processed_data import procees_data
        # name_file_download = f"{str(year)}{month}-divvy-tripdata.zip"
        # name_file_format = f"{str(year)}{month}-divvy-tripdata.csv"
            
        # if name_file_download not in os.listdir(folder_data):
        #     print(f"--- Data is crawling {name_file_download} ---")
        #     url = f"https://divvy-tripdata.s3.amazonaws.com/{name_file_download}"
FILE_SHARE = os.getenv('FILE_STORAGE', '/opt/file_storage/')
RAW_FOLDER = FILE_SHARE + 'raw/'
PROCESSED_FOLDER = FILE_SHARE + 'processed/'
URL_PREFIX = "https://divvy-tripdata.s3.amazonaws.com"

URL_TEMPLATE = URL_PREFIX +  '/{{ execution_date.strftime(\'%Y%m\') }}-divvy-tripdata.zip'
OUTPUT_FILE_ZIP = RAW_FOLDER + '{{ execution_date.strftime(\'%Y%m\') }}-divvy-tripdata.zip'

OUTPUT_FILE_CSV = RAW_FOLDER + '{{ execution_date.strftime(\'%Y%m\') }}-divvy-tripdata.csv'
OUTPUT_FILE_PROCESSED = PROCESSED_FOLDER + '{{ execution_date.strftime(\'%Y%m\') }}-divvy-tripdata_count'

local_workflow = DAG(
    "LocalIngestingDAG",
    schedule_interval="0 0 1 * *",
    start_date = datetime(2021, 12, 2),
    end_date = datetime(2022, 12, 30),
    catchup=True
)

with local_workflow:
    wget_task = BashOperator(
        task_id = "Wgetdata",
        # bash_command= F'curl -sSL {URL_TEMPLATE} > {OUTPUT_FILE}'
        bash_command = F'curl -sSL {URL_TEMPLATE} > {OUTPUT_FILE_ZIP}'
        # bash_command= 'echo Hello'
    )

    unzip_task = BashOperator(
        task_id ='Unzipdata',
        bash_command = F'unzip -o {OUTPUT_FILE_ZIP} -d {RAW_FOLDER}'
    )

    procees_task = PythonOperator(
        task_id="SparkProcessRawData",
        python_callable = procees_data,
        op_kwargs = dict(source=OUTPUT_FILE_CSV,
                         destination = OUTPUT_FILE_PROCESSED)
    )


    wget_task >> unzip_task >> procees_task