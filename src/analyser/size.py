class Size():
    def __init__(self, bytes):
        self.bytes = bytes

    def __repr__(self):
        if self.bytes < 1000:
            return f"{self.bytes} B"
        elif self.bytes < 1000000:
            return f"{self.bytes / 1000:.1f} KB"
        else:
            return f"{self.bytes / 1000000:.1f} MB"
        
    def __add__(self, other):
        return Size(self.bytes + other.bytes)
    
    def __eq__(self, other):
        return self.bytes == other.bytes