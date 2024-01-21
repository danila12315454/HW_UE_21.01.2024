import pytest

from src.circular_doubly_linked_list import CircularDoubleLinkedList, Node


def test_append() -> None:
    cdll = CircularDoubleLinkedList()
    for value in [10, 20, 30]:
        cdll.append(value)
    assert cdll.show() == "30 <- 10 -> 20 10 <- 20 -> 30 20 <- 30 -> 10 "


def test_prepend() -> None:
    cdll = CircularDoubleLinkedList()
    for value in [10, 20, 30][::-1]:
        cdll.prepend(value)
    assert cdll.show() == "30 <- 10 -> 20 10 <- 20 -> 30 20 <- 30 -> 10 "


def test_from_python_list() -> None:
    cdll = CircularDoubleLinkedList()

    cdll.from_python_list([10, 20, 30, 40, 100, 60])
    assert cdll.to_python_list() == [10, 20, 30, 40, 100, 60]

    cdll.from_python_list([103, "20", "303", 40, 10.30, 604])
    assert cdll.to_python_list() == [103, "20", "303", 40, 10.30, 604]


def test_delete_index() -> None:
    cdll = CircularDoubleLinkedList()

    cdll.from_python_list([10, 20, 30, 40, 100, 60])
    with pytest.raises(IndexError):
        cdll.delete_index(6)
    cdll.delete_index(0)
    cdll.delete_index(0)
    cdll.delete_index(1)
    cdll.delete_index(-1)
    assert cdll.to_python_list() == [30, 100]
    cdll.delete_index(-2)
    cdll.delete_index(-1)
    assert not cdll.to_python_list()
    with pytest.raises(IndexError):
        cdll.delete_index(-1)


def test_node_errors() -> None:
    node = Node(None)

    with pytest.raises(TypeError):
        node.set_next(None)  # type: ignore

    with pytest.raises(TypeError):
        node.set_previous(None)  # type: ignore


def test_set_item() -> None:
    cdll = CircularDoubleLinkedList()
    cdll.from_python_list([10, 20, 30, 40])
    cdll[0] = 100
    cdll[1] = "100"
    cdll[2] = None
    cdll[3] = 123.123

    assert cdll.to_python_list() == [100, "100", None, 123.123]

    cdll[-1] = 100
    cdll[-2] = "100"
    cdll[-3] = None
    cdll[-4] = 123.123

    assert cdll.to_python_list() == [100, "100", None, 123.123][::-1]

    with pytest.raises(IndexError):
        cdll[-5] = 123.123


def test_get_item() -> None:
    test_list = [10, 20, 30, 40, 5]
    cdll = CircularDoubleLinkedList()
    cdll.from_python_list(test_list)
    assert all(  # pylint: disable=R1729
        [test_list[i] == cdll[i] for i in range(len(cdll))]
    )
    assert all(  # pylint: disable=R1729
        [test_list[i] == cdll[i] for i in range(-len(cdll), 1)]
    )

    with pytest.raises(IndexError):
        print(cdll[-6])
