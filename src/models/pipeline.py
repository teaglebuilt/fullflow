import copy
from itertools import chain
from typing import Iterable, Union, List
from .node import Node
import yaml



class Pipeline:

    def __init__(self,
        name: str,
        nodes: Iterable[Union[Node, "Pipeline"]]
    ) -> None:
        self._nodes = nodes

    def workflow(self, workflow):
        with open(workflow, 'r') as file:
            return yaml.load(file, Loader=yaml.SafeLoader)

    @property
    def nodes(self) -> List[Node]:
        return copy.copy(self._nodes)