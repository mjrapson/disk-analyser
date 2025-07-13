from .node import Node
from .node_type import NodeType

class File(Node):
    def __init__(self, name, size):
        super().__init__(name=name)
        self.size = size

    def get_type(self):
        return NodeType.FILE
    
    def get_size(self):
        return self.size
    
    def __repr__(self):
        return f"{self.name}"
    