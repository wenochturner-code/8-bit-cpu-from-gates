class RAM:
    def __init__(self, size):
        self.cells = [[0]*8 for _ in range(size)]
    
    def write(self, address, data):
        self.cells[address] = data
        
    def read(self, address):
        return self.cells[address]
    