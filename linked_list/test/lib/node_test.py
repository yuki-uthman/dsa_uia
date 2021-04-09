import pytest
from lib.node import Node


def test_data():
    node = Node(data=1)
    assert node.data == 1


def test_next():
    tail = Node(data=3)
    middle = Node(data=2, n_node=tail)
    node = Node(data=1, n_node=middle)

    assert node.next == middle
    assert node.next.next == tail


def test_is_tail():
    tail = Node()
    assert tail.is_tail() == True

    non_tail = Node(n_node=Node())
    assert non_tail.is_tail() == False
