from airflow.plugins_manager import AirflowPlugin
from src.operators.kernel import KernelOperator
from src.hooks.kernel import KernelGateway


class FullFlowPlugin(AirflowPlugin):
    """fullflow interface for airflow"""
    name = "fullflow"
    operators = [KernelOperator]
    hooks = [KernelGateway]