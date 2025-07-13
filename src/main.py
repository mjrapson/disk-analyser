from src.analyser.analyser import analyse
from src.analyser.node_type import NodeType

import argparse

def print_tree(root, max_depth, max_breadth, depth = 0, prefix=""):
    curr_breadth = 0
    if depth == 0:
        print(f"{root.name}/ ({root.get_size()})")

    for child in root.children:
        if child.get_type() == NodeType.FILE:
            if curr_breadth < max_breadth:
                print(f"{prefix}|-- {child.name} ({child.get_size()})")
            elif curr_breadth == max_breadth:
                print(f"{prefix}|-- (...)")
            curr_breadth += 1
        elif child.get_type() == NodeType.DIRECTORY:
            if depth < max_depth:
                print(f"{prefix}|-- {child.name}")
                print_tree(child, max_depth, max_breadth, depth + 1, prefix=f"|{prefix}   ")
        else:
            print("unknown type")

def main():
    arg_parser = argparse.ArgumentParser(prog="Disk Analyser")
    arg_parser.add_argument("--dir", required=True, help="Root folder to analyse")
    args = arg_parser.parse_args()

    print(f"Scanning {args.dir}...")
    root = analyse(args.dir)
    print_tree(root, 1, 3)


if __name__ == "__main__":
    main()