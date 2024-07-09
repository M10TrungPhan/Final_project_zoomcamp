from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
        # name_file_download = f"{str(year)}{month}-divvy-tripdata.zip"
        # name_file_format = f"{str(year)}{month}-divvy-tripdata.csv"
            
        # if name_file_download not in os.listdir(folder_data):
        #     print(f"--- Data is crawling {name_file_download} ---")
        #     url = f"https://divvy-tripdata.s3.amazonaws.com/{name_file_download}"
FILE_SHARE = os.getenv('FILE_STORAGE', '/opt/file_storage/')
URL_PREFIX = "https://divvy-tripdata.s3.amazonaws.com"

URL_TEMPLATE = URL_PREFIX +  '/{{ execution_date.strftime(\'%Y-%m\') }}-divvy-tripdata.zip'
OUTPUT_FILE = FILE_SHARE + '{{ execution_date.strftime(\'%Y-%m\') }}-divvy-tripdata.zip'

local_workflow = DAG(
    "LocalIngestingDAG",
    schedule_interval="0 0 1 * *",
    start_date = datetime(2021, 12, 2),
    # end_date = datetime(2023, 12, 30),
    catchup=False
)

with local_workflow:
    wget_task = BashOperator(
        task_id = "Wgetdata",
        # bash_command= F'curl -sSL {URL_TEMPLATE} > {OUTPUT_FILE}'
        bash_command = F'curl -sSL https://divvy-tripdata.s3.amazonaws.com/202301-divvy-tripdata.zip > {OUTPUT_FILE}'
        # bash_command= 'echo Hello'
    )

    unzip_task = BashOperator(
        task_id ='Unzipdata',
        bash_command = f'echo "{{execution_date }}" {URL_TEMPLATE} '
    )


    wget_task >> unzip_task