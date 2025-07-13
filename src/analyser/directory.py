from .node import Node
from .node_type import NodeType
from .size import Size

class Directory(Node):
    def __init__(self, name):
        super().__init__(name=name)
        self.children = []

    def get_type(self):
        return NodeType.DIRECTORY
    
    def get_size(self):
        size = Size(0)
        for child in self.children:
            size += child.get_size()
        return size
    
    def __repr__(self):
        return f"{self.name}"
    