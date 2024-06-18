import json
from abc import ABC, abstractmethod
from typing import List
from visitor import IVisitor
from node import InternalNode
from node import LeafNode
from node import Node
from icon import DefaultIcon
from icon import PokerFaceIcon
from icon import Icon

class Style(ABC):
    def __init__(self, file_name: str, icon_style: str):
        self.root = self.load_data(file_name, "root")
        self.icon = self.choose_icon(icon_style)

    def load_data(self, file_name: str, node_name: str) -> Node:
        try:
            with open(file_name, 'r') as file:
                json_data = json.load(file)
            return self.build_data(json_data, node_name)
        except (IOError, json.JSONDecodeError) as e:
            print(e)
            return None

    def build_data(self, json_data: dict, node_name: str) -> Node:
        if json_data is None:
            return None

        if not json_data:
            return LeafNode(node_name, "null")

        node = InternalNode(node_name)
        for key, value in json_data.items():
            if isinstance(value, dict):
                child_node = self.build_data(value, key)
                if child_node:
                    node.add_child(child_node)
            else:
                node.add_child(LeafNode(key, str(value)))
        return node

    def choose_icon(self, icon_style: str):
        if icon_style == "pokerface":
            icon = PokerFaceIcon()
        elif icon_style == "default":
            icon = DefaultIcon()
        else:
            icon = DefaultIcon()
        return icon



    @abstractmethod
    def accept(self, visitor):
        pass

class TreeStyle(Style):
    def __init__(self, file_name: str, icon_style: str):
        super().__init__(file_name, icon_style)
    def accept(self, visitor: IVisitor):
        visitor.visit_tree(self)


class RectangleStyle(Style):
    def __init__(self, file_name: str, icon_style: str):
        super().__init__(file_name, icon_style)

    

    def accept(self, visitor: IVisitor):
        visitor.visit_rectangle(self)