from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Node = None  # type: ignore
        self.previous: Node = None  # type: ignore

    def set_next(self, next_node: "Node") -> None:
        if not isinstance(next_node, Node):
            raise TypeError("Expected Node")
        self.next = next_node

    def set_previous(self, previous_node: "Node") -> None:
        if not isinstance(previous_node, Node):
            raise TypeError("Expected Node")
        self.previous = previous_node

    def show(self) -> str:
        return f"{self.previous.value} <- {self.value} -> {self.next.value}"


class CircularDoubleLinkedList:
    def __init__(self) -> None:
        self.root: Node = None  # type: ignore
        self.length: int = 0

    def __setitem__(self, key: int, value: Any) -> None:
        if 0 <= key < self.length:
            node_to_change = self.root.previous
            for _ in range(key + 1):
                node_to_change = node_to_change.next
            node_to_change.value = value
        elif -self.length <= key < 0:
            node_to_change = self.root
            for _ in range(-key):
                node_to_change = node_to_change.previous
            node_to_change.value = value
        else:
            raise IndexError("Index out of range")

    def __getitem__(self, key: int) -> Any:
        if 0 <= key < self.length:
            node_to_change = self.root.previous
            for _ in range(key + 1):
                node_to_change = node_to_change.next
            return node_to_change.value
        if -self.length <= key < 0:
            node_to_change = self.root
            for _ in range(-key):
                node_to_change = node_to_change.previous
            return node_to_change.value
        raise IndexError("Index out of range")

    def __len__(self) -> int:
        return self.length

    def show(self) -> str:
        return_string = ""
        node_to_show = self.root
        for _ in range(self.length):
            return_string += node_to_show.show() + " "
            node_to_show = node_to_show.next
        return return_string

    def from_python_list(self, python_list: list[Any]) -> None:
        self.root = None  # type: ignore
        for value in python_list:
            self.append(value)

    def to_python_list(self) -> list[Any]:
        return_list = []
        node_to_show = self.root
        for _ in range(self.length):
            return_list.append(node_to_show.value)
            node_to_show = node_to_show.next
        return return_list

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.root is None:
            new_node.set_next(new_node)
            new_node.set_previous(new_node)
            self.root = new_node
            self.length = 1
        elif self.length == 1:
            new_node.set_next(self.root)
            new_node.set_previous(self.root.previous)
            self.root.set_previous(new_node)
            self.root.set_next(new_node)
            self.length += 1
        else:
            new_node.set_next(self.root)
            new_node.set_previous(self.root.previous)
            self.root.previous.set_next(new_node)
            self.root.set_previous(new_node)
            self.length += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value)
        if self.root is None:
            new_node.set_next(new_node)
            new_node.set_previous(new_node)
            self.root = new_node
            self.length = 1
        elif self.length == 1:
            new_node.set_next(self.root)
            new_node.set_previous(self.root.previous)
            self.root.set_previous(new_node)
            self.root.set_next(new_node)
            self.root = new_node
            self.length += 1
        else:
            new_node.set_next(self.root)
            new_node.set_previous(self.root.previous)
            self.root.previous.set_next(new_node)
            self.root.set_previous(new_node)
            self.root = new_node
            self.length += 1

    def delete_index(self, key: Any) -> None:
        if self.length == 1:
            self.root = None  # type: ignore
            self.length -= 1
            return
        if self.length == 0:
            raise IndexError("List is empty")
        if 0 <= key < self.length:
            node_to_change = self.root.previous
            for _ in range(key + 1):
                node_to_change = node_to_change.next

            node_to_change.previous.set_next(node_to_change.next)
            node_to_change.next.set_previous(node_to_change.previous)
            if node_to_change == self.root:
                self.root = node_to_change.next
            self.length -= 1
        elif -self.length <= key < 0:
            node_to_change = self.root
            for _ in range(-key):
                node_to_change = node_to_change.previous
            node_to_change.previous.set_next(node_to_change.next)
            node_to_change.next.set_previous(node_to_change.previous)
            if node_to_change == self.root:
                self.root = node_to_change.next
            self.length -= 1
        else:
            raise IndexError("Index out of range")
