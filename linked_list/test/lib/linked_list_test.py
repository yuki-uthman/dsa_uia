import pytest
from lib.linked_list import LinkedList
from lib.node import Node


@pytest.fixture
def list_empty():
    return LinkedList()


@pytest.fixture
def list_one():
    node = Node(data=1)
    return LinkedList(head=node)


@pytest.fixture
def list_three():
    tail = Node(data=3)
    middle = Node(data=2, n_node=tail)
    head = Node(data=1, n_node=middle)
    return LinkedList(head=head)


def test_count(list_three):
    assert list_three.count() == 3


def test_is_empty(list_empty, list_one, list_three):
    assert list_empty.is_empty() == True
    assert list_one.is_empty() == False
    assert list_three.is_empty() == False


def test_max(list_empty, list_one, list_three):
    assert list_one.max() == 1
    assert list_three.max() == 3


def test_min(list_empty, list_one, list_three):
    assert list_one.min() == 1
    assert list_three.min() == 1


def test_tail(list_one, list_three):
    assert list_one.get_tail().data == 1
    assert list_three.get_tail().data == 3


def test_append_empty(list_empty):
    list_empty.append(1)
    assert list_empty.head.data == 1

    list_empty.append(2)
    assert list_empty.head.data == 1
    assert list_empty.get_tail().data == 2


def test_append(list_three):
    list_three.append(0)
    assert list_three.get_tail().data == 0


def test_prepend(list_empty):
    list_empty.prepend(1)
    assert list_empty.head.data == 1

    list_empty.prepend(2)
    assert list_empty.head.data == 2
    assert list_empty.head.next.data == 1


def test_delete(list_one, list_three):
    list_one.delete(1)
    assert list_one.is_empty()

    list_three.delete(2)
    assert list_three.to_list() == [1, 3]

    list_three.delete(3)
    assert list_three.to_list() == [1]

    list_three.delete(1)
    assert list_three.is_empty()


def test_pop(list_one, list_three):
    list_one.pop()
    assert list_one.to_list() == []

    list_three.pop()
    assert list_three.to_list() == [1, 2]

    list_three.pop()
    assert list_three.to_list() == [1]


def test_pop_return(list_three):
    assert list_three.pop() == 3
    assert list_three.pop() == 2
    assert list_three.pop() == 1


def test_pop_left(list_one, list_three):
    list_one.pop_left()
    assert list_one.to_list() == []

    list_three.pop_left()
    assert list_three.to_list() == [2, 3]

    list_three.pop_left()
    assert list_three.to_list() == [3]


def test_pop__left_return(list_three):
    assert list_three.pop_left() == 1
    assert list_three.pop_left() == 2
    assert list_three.pop_left() == 3


def test_to_list(list_empty, list_one, list_three):
    assert list_one.to_list() == [1]
    assert list_three.to_list() == [1, 2, 3]

    assert list_one.to_list(reverse=True) == [1]
    assert list_three.to_list(reverse=True) == [3, 2, 1]


def test_print_list(capsys, list_one, list_three):
    list_one.print_list()
    assert capsys.readouterr().out == "|1|-->"

    list_three.print_list()
    assert capsys.readouterr().out == "|1|-->|2|-->|3|-->"


def test_print_list_reverse(capsys, list_one, list_three):
    list_one.print_list(True)
    assert capsys.readouterr().out == "|1|-->"

    list_three.print_list(True)
    assert capsys.readouterr().out == "|3|-->|2|-->|1|-->"
