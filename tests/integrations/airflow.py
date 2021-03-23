# from datetime import date, datetime, timedelta
# from airflow.models.dagrun import DagRunType
# from airflow.operators.python import PythonOperator
# from airflow.utils.state import State
# from airflow.decorators import task
# from airflow.utils import timezone
# from src.models import Node
# import pytest

# DEFAULT_DATE = timezone.datetime(2016, 1, 1)
# END_DATE = timezone.datetime(2016, 1, 2)
# INTERVAL = timedelta(hours=12)
# FROZEN_NOW = timezone.datetime(2016, 1, 2, 12, 1, 1)


# def test_airflow_input(airflow_dag, airflow_operator):
#     node = Node('airflow_task', ['hello', 'world'], airflow_operator)
