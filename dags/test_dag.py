import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.docker_operator import DockerOperator
from airflow.models import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago


@task
def choose_operator():
    print("Choose Operator based off of environment")
    return os.environ['OPERATOR']

@task()
def end():
    print("ending") 


with DAG(
   "test_dag",
   start_date=days_ago(1),
   schedule_interval=None,
) as dag:

    setup_client_in_k8 = KubernetesPodOperator(
        namespace='default', 
        image="python:3.8", 
        cmds=["python","-c"], 
        arguments=["print('hello world')"], 
        name="setup_client-test", 
        task_id="kubernetes", 
        labels={"client": "hphc"},
        get_logs=True, 
        in_cluster=True, 
        dag=dag 
    )

    setup_client_in_swarm = DockerOperator(
        dag=dag,
        task_id='docker',
        image='teaglebuilt/airflow:local',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        command='python extract_from_api_or_something.py'
    )


    choose_operator >> [setup_client_in_k8, setup_client_in_swarm] >> end
