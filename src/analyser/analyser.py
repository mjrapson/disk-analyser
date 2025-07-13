from .directory import Directory
from .file import File
from .node_type import NodeType
from .size import Size

import os

def by_type(node):
    return (node.get_type().value, node.name.lower())

def sort(root):
    root.children = sorted(root.children, key=by_type)
    for child in root.children:
        if child.get_type() == NodeType.DIRECTORY:
            sort(child)

def analyse(path):
    if path == "":
        raise ValueError("Path is empty")
    
    if not os.path.exists(path):
        raise ValueError("Path does not exist")
    
    if not os.path.isdir(path):
        raise ValueError("Path is not a directory")
    
    root = Directory(os.path.basename(path))

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            subdir = analyse(item_path)
            root.children.append(subdir)
        elif os.path.isfile(item_path):
            file = File(os.path.basename(item_path), Size(os.path.getsize(item_path)))
            root.children.append(file)

    return root