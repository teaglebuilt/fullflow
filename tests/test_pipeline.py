from unittest import TestCase
from src.models import Pipeline, Node


def one():
    return 'one'

def two():
    return 'two'

def three():
    return 'three'


class TestPipeline(TestCase):

    def setUp(self):
        self.nodes = [
            Node('nodeOne', ['helloOne'], callable(one)),
            Node('nodeTwo', ['helloTwo'], callable(two)),
            Node('nodeThree', ['helloThree'], callable(three))
        ]
        self.pipeline = Pipeline('test_pipeline', self.nodes)

    def test_pipeline_return_nodes(self):
        self.assertEquals(len(self.pipeline.nodes), 3)