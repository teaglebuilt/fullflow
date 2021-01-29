from airflow.hooks.base_hook import BaseHook
from airflow.models import Connection


class KernelGateway(BaseHook):

    def __init__(self, conn_id):
        super().__init__(conn_id)
        self.gateway = self.get_connection(conn_id)

    def get_kernels(self):
        pass