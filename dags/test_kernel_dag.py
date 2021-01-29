import os
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from src.operators.kernel import KernelOperator


@dag(default_args={"owner": "airflow"}, schedule_interval=None, start_date=days_ago(2), tags=['kernel'])
def jupyter_powered_pipeline():

    @task
    def start():
        print('starting')

    KernelOperator(
        task_id='run_model',
        conn=os.environ['GATEWAY'],
        kernel="python"
    )

dag = jupyter_powered_pipeline()