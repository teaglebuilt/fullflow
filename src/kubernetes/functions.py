import os
import yaml
from kubernetes import client, config
from jinja2 import FileSystemLoader, Environment
from airflow.kubernetes.pod_generator import PodGenerator
from airflow.kubernetes.k8s_model import K8SModel

def generate_kernel_pod_yaml(keywords):
    """Return the kubernetes pod spec as a yaml string.

    - load jinja2 template from this file directory.
    - substitute template variables with keywords items.
    """
    j_env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)), trim_blocks=True, lstrip_blocks=True)
    k8s_yaml = j_env.get_template('/kernel-pod.yaml.j2').render(**keywords)
    return k8s_yaml



def launch_kubernetes_kernel(kernel):
    config.load_incluster_config()
    keywords = dict()
    breakpoint()
    keywords['kernel_name'] = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    keywords['kernel_id'] = kernel['id']
    keywords['eg_response_address'] = os.environ['GATEWAY']
    keywords['kernel_spark_context_init_mode'] = ""

    for name, value in os.environ.items():
        if name.startswith('KERNEL_'):
            keywords[name.lower()] = yaml.safe_load(value)

    k8s_yaml = generate_kernel_pod_yaml(keywords)
    # PodGenerator(pod=)