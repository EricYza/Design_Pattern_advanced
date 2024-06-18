import json
from abc import ABC, abstractmethod
from typing import List
from icon import DefaultIcon
from icon import PokerFaceIcon
from icon import Icon
from node import InternalNode
from node import LeafNode
from node import Node



#定义访问者接口
class IVisitor(ABC):
    @abstractmethod
    def visit_tree(self, tree_style):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle_style):
        pass

#实现访问者类
class Visitor(IVisitor):
    def visit_tree(self, tree_style):
        self.show_tree(tree_style)

    def visit_rectangle(self, rectangle_style):
        self.show_rectangle(rectangle_style)

    def show_tree(self, tree_style):
        children = tree_style.root.get_children()
        num_children = len(children)
        for index, child in enumerate(children):
            self.display_tree(child, 0, [index == num_children - 1], tree_style)

    def display_tree(self, node: Node, level: int, is_last_child: List[bool], tree_style):
        for i in range(level):
            if not is_last_child[i]:
                print('|' + f"{' ' * 2}", end="")
            else:
                print(f"{' ' * 3}", end="")
        if not is_last_child[level]:
            if node.is_internal():
                print("├─" + tree_style.icon.get_internal_node_icon() + node.get_representation())
            else:
                print("├─" + tree_style.icon.get_leaf_node_icon() + node.get_representation())
        else:
            if node.is_internal():
                print("└─" + tree_style.icon.get_internal_node_icon() + node.get_representation())
            else:
                print("└─" + tree_style.icon.get_leaf_node_icon() + node.get_representation())
        if isinstance(node, InternalNode):
            for child_index, child in enumerate(node.get_children()):
                is_last_child.append(child_index == len(node.get_children()) - 1)
                self.display_tree(child, level + 1, is_last_child, tree_style)
                is_last_child.pop()


    def show_rectangle(self, rectangle_style) -> None:
        children = rectangle_style.root.get_children()
        num_children = len(children)
        for index, child in enumerate(children):
            self.display_rectangle(child, 0, [index == num_children - 1], index == 0, rectangle_style)

    def display_rectangle(self, node: Node, level: int, is_last_child: List[bool], is_head, rectangle_style):
        is_toil = True
        if is_last_child[level]:
            if len(node.get_children()) != 0:
                is_toil = False
            else:
                for i in range(level):
                    if not is_last_child[i]:
                        is_toil = False
        else:
            is_toil = False
        if node.is_internal():
            icon = rectangle_style.icon.get_internal_node_icon()
        else:
            icon = rectangle_style.icon.get_leaf_node_icon()
        if is_head:
            representation = '┌─' + icon + node.get_representation() + ' '
            print(representation + f"{'─' * (50 - len(representation))}" + '┐')
        elif is_toil:
            representation = ""
            for i in range(level):
                representation += '└──'
            representation += '└─' + icon + node.get_representation() + ' '
            print(representation + f"{'─' * (50 - len(representation))}" + '┘')            
        else:
            representation = str('|' + f"{' ' * 2}") * level + "├─" + icon + node.get_representation() + ' '
            print(representation + f"{'─' * (50 - len(representation))}" + '┤')
        if isinstance(node, InternalNode):
            for child_index, child in enumerate(node.get_children()):
                is_last_child.append(child_index == len(node.get_children()) - 1)
                self.display_rectangle(child, level + 1, is_last_child, False, rectangle_style)
                is_last_child.pop()
