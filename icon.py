from abc import ABC, abstractmethod

class Icon(ABC):
    @abstractmethod
    def get_internal_node_icon(self):
        pass

    @abstractmethod
    def get_leaf_node_icon(self):
        pass

class DefaultIcon(Icon):
    def get_internal_node_icon(self):
        return " "

    def get_leaf_node_icon(self):
        return " "

class PokerFaceIcon(Icon):
    def get_internal_node_icon(self):
        return "♢"

    def get_leaf_node_icon(self):
        return "♤"
