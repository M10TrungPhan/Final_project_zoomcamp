from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
from airflow.models.param import Param
FILE_SHARE = os.getenv('FILE_STORAGE', '/opt/file_storage/')
OUTPUT_FILE = FILE_SHARE + '{{ execution_date.strftime(\'%Y_%m_%d_%H_%M_%S \') }}'
test_content = "{{ execution_date }}" 
test_dag = DAG(
    'TestDag',
    schedule ="@monthly",
    start_date = datetime(2020, 9, 2),     
    params={
         "x": Param(5, type="integer", minimum=3),
         "my_int_param": 6
     },
    # data_interval_start=datetime(2021,1,1),
    # end_date = datetime(2023, 1, 1),
    catchup=True
)

with test_dag:
    dag_task_test_1 = BashOperator(
        task_id = "Task1",
        # bash_command = F'curl -sSL {URL_TEMPLATE} > {OUTPUT_FILE}'
        bash_command=F'echo {test_content} > {OUTPUT_FILE}'
    ) 

    dag_task_test_2 = BashOperator(
        task_id='Task2',
        bash_command = 'echo "{{ execution_date }}" '
    )
    

    dag_task_test_1 >> dag_task_test_2
