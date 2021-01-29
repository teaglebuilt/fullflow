import os
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from src.hooks.kernel import KernelGateway
from src.mixins.gateway import GatewayHandler


class KernelOperator(BaseOperator, GatewayHandler):
    """Kernel Gateway Interface to Airflow"""
    @apply_defaults
    def __init__(self, conn, kernel, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = conn
        self.kernelSpec = open(
            f"{os.environ['AIRFLOW_HOME']}/src/kernels/{kernel}.json"
        )

    def get_hook(self) -> KernelGateway:
        return KernelGateway(
            self.conn
        )

    def execute(self, context):
        self.log.info('Executing Kernel')
        breakpoint()
        