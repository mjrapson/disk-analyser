class Node():
    def __init__(self, name):
        self.name = name

    def get_type(self):
        raise NotImplementedError
    
    def get_size(self):
        raise NotImplementedError

    