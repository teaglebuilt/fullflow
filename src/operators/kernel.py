import os
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from src.hooks.kernel import KernelGateway
from src.kubernetes.functions import launch_kubernetes_kernel
from kubernetes.client import models as k8s


class KernelOperator(BaseOperator):
    """Kernel Gateway Interface to Airflow"""
    @apply_defaults
    def __init__(self, conn, kernel, **kwargs):
        breakpoint()
        super().__init__(**kwargs)
        self.conn = conn
        self.kernelSpec = open(
            f"{os.environ['AIRFLOW_HOME']}/src/kernels/{kernel}.json"
        )
        self.kernel = kernel

    def get_hook(self) -> KernelGateway:
        return KernelGateway(
            self.conn
        )

    def execute(self, context):
        self.log.info('Executing Kernel')
        client: KernelGateway = self.get_hook()
        kernels = client.get_kernels()
        python_kernel = client.start_kernel(self.kernel)
        launch_kubernetes_kernel(python_kernel)
        breakpoint()

        