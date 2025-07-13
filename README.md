# Disk Analyser

boot.dev project build using python. Walks a given directory recursively and generates a disk space report on the CLI

# Features
- Generates a size report for a given directory
- Can report custom depth and breadth
- Formats file sizes appropriately
- Sorts by type alphabetically

# Example
Default depth and breadth
```
disk-analyser/ (73.0 KB)
|-- .git/ (47.7 KB)
|-- src/ (19.2 KB)
|-- tests/ (6.0 KB)
|-- .gitignore (12 B)
|-- README.md (52 B)
|-- run.sh (28 B)
|-- (...)
```

Expanded depth
```
disk-analyser/ (73.0 KB)
|-- src/ (19.2 KB)
|   |-- __pycache__/ (7.5 KB)
|   |-- analyser/ (10.0 KB)
|   |-- __init__.py (0 B)
|   |-- main.py (1.7 KB)
|-- tests/ (6.0 KB)
|   |-- __pycache__/ (4.5 KB)
|   |-- test_analyser.py (301 B)
|   |-- test_directory.py (597 B)
|   |-- test_file.py (240 B)
|   |-- (...)
|-- .gitignore (12 B)
|-- README.md (52 B)
|-- run.sh (28 B)
|-- (...)
```

# Future
- More sorting options (e.g. size ascending/descending)
- Report filters (by file type, extension or name)
- Export for use in graphical application