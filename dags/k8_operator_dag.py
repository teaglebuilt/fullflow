import os
from airflow.models import DAG
from airflow_kubernetes_job_operator.kubernetes_job_operator import KubernetesJobOperator
from airflow_kubernetes_job_operator.kubernetes_legacy_job_operator import KubernetesLegacyJobOperator
from airflow.utils.dates import days_ago
from airflow.models.baseoperator import BaseOperator


default_args = {
    "owner": "tester",
    "start_date": days_ago(2),
    "retries": 0
}


dag = DAG(
   "job-tester",
   default_args=default_args,
   description="Test base job operator",
   schedule_interval=None
)

job_task = KubernetesJobOperator(
    task_id="teaglebuilt/fullflow:dev",
    dag=dag,
    image="ubuntu",
    command=["bash", "-c", 'echo "all ok"'],
)

job_task_from_yaml = KubernetesJobOperator(
    dag=dag,
    task_id="from-yaml",
    body_filepath=f"{os.environ['AIRFLOW_HOME']}/k8s/jobs/dummy.yaml"
)

# Legacy compatibility to KubernetesPodOperator
legacy_job_task = KubernetesLegacyJobOperator(
    task_id="legacy-image-job",
    image="ubuntu",
    cmds=["bash", "-c", 'echo "all ok"'],
    dag=dag,
    is_delete_operator_pod=True,
)