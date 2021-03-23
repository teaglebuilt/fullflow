import copy
import logging
from collections import defaultdict
from typing import Iterable, Union, List, Set, Tuple
import yaml
from .node import Node



class Pipeline:
    """Primary class for Fullflow Pipeline"""
    def __init__(self,
        name: str,
        nodes: Iterable[Union[Node, "Pipeline"]]
    ) -> None:
        self._logger = logging.getLogger(__name__)
        self._name = name
        self._nodes = nodes
        self._nodes_by_input = defaultdict(set)
        self._nodes_by_output = {}


    def workflow(self, workflow):
        with open(workflow, 'r') as file:
            return yaml.load(file, Loader=yaml.SafeLoader)

    @property
    def nodes(self) -> List[Node]:
        return copy.copy(self._nodes)

    @property
    def name(self) -> str:
        return self._name

    def node_dependencies(self) -> Set[Tuple[Node, Node]]:
        pass

    def __repr__(self):
        reprs = [repr(node) for node in self.nodes]
        return "{}([\n{}\n])".format(self.__class__.name, ",\n".join(reprs))

    def __add__(self, other):
        if not isinstance(other, Pipeline):
            return NotImplemented
        return Pipeline(set(self.nodes + other.nodes))