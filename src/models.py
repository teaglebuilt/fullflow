import os
import yaml
from kubernetes import client, config
from airflow.kubernetes.pod_launcher import PodLauncher

def launch_kubernetes_kernel(kernel_id, address, context):
    config.load_incluster_config()

    keywords = dict()
    keywords['kernel_name'] = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    keywords['kernel_id'] = kernel_id
    keywords['eg_response_address'] = address
    keywords['kernel_spark_context_init_mode'] = context

    for name, value in os.environ.items():
        if name.startswith('KERNEL_'):
            keywords[name.lower()] = yaml.safe_load(value)