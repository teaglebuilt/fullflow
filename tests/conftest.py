from airflow.models import DAG
from airflow.operators.python import PythonOperator
from src.models import Node
from pytest import fixture


@fixture
def airflow_dag():
    dag = DAG(
        dag_id='airflow_test_dag',
        schedule_interval=None,
        default_args={'owner': 'airflow'}
    )
    yield dag


@fixture
def airflow_operator():
    yield PythonOperator(
        task_id='python_operator',
        python_callable=two
    )