from src.models import Node
import pytest

def out():
    return "output"


def one(input1: str):
    return input1


def two(input1: str, input2: str):
    return input1 + input2


def three(input1: str, input2: str, input3: str):
    return input1 + input2 + input3


def test_node_run():
    node = Node('node1', ['hello', 'world'], two)
    assert node.run() == 'helloworld'

def test_output(capsys):
    stdout, stderr = capsys.readouterr()