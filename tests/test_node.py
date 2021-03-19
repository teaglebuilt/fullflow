from unittest import TestCase
from src.models import Node


class TestNode(TestCase):

    def test_node_is_callable(self):
        def word():
            return 'poop'

        assert Node(
            'test_node', None, func=callable(word)
        )._func is True