from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from src.hooks.kernel import KernelGateway


class KernelOperator(BaseOperator):
    """Kernel Gateway Interface to Airflow"""
    @apply_defaults
    def __init__(self, conn, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conn = conn

    def get_hook(self) -> KernelGateway:
        return KernelGateway(
            self.conn
        )

    def execute(self, context):
        self.log.info('Executing Kernel')