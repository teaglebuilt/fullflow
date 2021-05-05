from airflow.models import DAG
from pytest import fixture


@fixture
def airflow_dag():
    dag = DAG(
        dag_id='airflow_test_dag',
        schedule_interval=None,
        default_args={'owner': 'airflow'}
    )
    yield dag

