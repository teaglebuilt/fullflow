import logging
from typing import Callable, Iterable, Dict, Any, Union, List


class Node:
    def __init__(
        self,
        name,
        params: Union[None, Any],
        func: Callable,
        tags: Iterable[str] = None
    ) -> None:
        self._func = func
        self._name = name
        self._params = params
        self._output = None
        self._tags = set([] if tags is None else tags)

    def _logger(self):
        return logging.getLogger(__name__)

    @property
    def params(self) -> List[str]:
        return self.params

    @property
    def output(self) -> List[str]:
        return self._output

    def run(self):
        return self._func(*self._params)

    def __repr__(self):
        return "Node({}, {!r}, {!r}, {!r})".format(
            self._func.__name__, self._params, self._output, self._name
        )

    def __eq__(self, other):
        keys = {"_params", "_output", "_func", "_name"}
        return all(self.__dict__[k] == other.__dict__[k] for k in keys)

    def __hash__(self):
        return hash((tuple(self._params), tuple(self._output), self._name))