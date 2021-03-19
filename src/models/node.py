import logging
from typing import Callable, Iterable, Dict, Any, Union


class Node:
    def __init__(
        self,
        name,
        inputs: Union[None, Any],
        func: Callable,
        tags: Iterable[str] = None
    ) -> None:
        self._func = func
        self._name = name
        self._inputs = inputs
        self._tags = set([] if tags is None else tags)

    def _logger(self):
        return logging.getLogger(__name__)

    def run(self, inputs: Dict[str, any] = None) -> Dict[str, Any]:
        return dict({'output': 'yes'})