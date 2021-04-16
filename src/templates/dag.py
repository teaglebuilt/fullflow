from typing import Union, Optional
from datetime import datetime
from pydantic import BaseModel
from airflow import DAG
from src.core import Template


class Dag(Template):
    template: '''
    from airflow.models import DAG, TaskInstance
    from airflow.contrib.operators import kubernetes_pod_operator


    with DAG(
        dag_id='{{ dag.name }}',
        default_args={'owner': '{{ owner }}'},
        schedule_interval='{{ cron_expression }}',
        start_date={{ start_date.__repr__() }}
    ) as dag:
    {% for node in nodes %}
        {{ node.task_id }} = KubernetesPodOperator(
            task_id={{ node.task_id }},
            name={{ node.name }},
            image=={{ node.image }},
            cmds={{ node.commands }},
            volume_mounts={{ node.mounts }},
            volumes={{ node.volumes }},
            config_file={{ environment.config }}
        )
    {% endfor %}
    '''
    dag: Union[DAG, dict]
    owner: str = 'fullflow'
    start_date: Optional[datetime] = None

    def __post_init__(self):
        if isinstance(self.dag, dict):
            self.dag = DAG.parse_obj(self.dag)

    def nodes(self):
        for node_name, node in self.dag.nodes.items():
            yield NodeTask(name=node_name, node=node)
