import os
import yaml
from jinja2 import FileSystemLoader, Environment
from airflow.kubernetes.pod_generator import PodGenerator
from airflow.kubernetes.k8s_model import K8SModel
from airflow.kubernetes.kube_client import client, config



def generate_kernel_pod_yaml(keywords):
    """Return the kubernetes pod spec as a yaml string.

    - load jinja2 template from this file directory.
    - substitute template variables with keywords items.
    """
    j_env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)), trim_blocks=True, lstrip_blocks=True)
    k8s_yaml = j_env.get_template('/kernel-pod.yaml.j2').render(**keywords)
    return k8s_yaml



def launch_kubernetes_kernel(kernel):
    """launch pod for associated kernel"""
    config.load_incluster_config()
    keywords = dict()
    keywords['kernel_name'] = kernel['name']
    keywords['kernel_id'] = kernel['id']
    keywords['eg_response_address'] = os.environ['GATEWAY']

    for name, value in os.environ.items():
        if name.startswith('KERNEL_'):
            keywords[name.lower()] = yaml.safe_load(value)

    k8s_yaml = generate_kernel_pod_yaml(keywords)
    k8s_objs = yaml.safe_load_all(k8s_yaml)
    client.CoreV1Api(client.ApiClient()).create_namespaced_pod(body=k8s_objs)