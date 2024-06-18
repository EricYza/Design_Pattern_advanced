from abc import ABC, abstractmethod
from typing import List

class Node(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def is_internal(self) -> bool:
        pass

    @abstractmethod
    def get_representation(self) -> str:
        pass

    @abstractmethod
    def get_children(self) -> List['Node']:
        pass

class InternalNode(Node):
    def __init__(self, name: str):
        super().__init__(name)
        self.children = []

    def add_child(self, child: Node):
        self.children.append(child)

    def get_children(self) -> List[Node]:
        return self.children

    def is_internal(self) -> bool:
        return True

    def get_representation(self) -> str:
        return self.name
    
class LeafNode(Node):
    def __init__(self, name: str, value: str):
        super().__init__(name)
        self.value = value

    def is_internal(self) -> bool:
        return False

    def get_representation(self) -> str:
        return f"{self.name}: {self.value}"

    def get_children(self) -> List[Node]:
        return []