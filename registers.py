class Register:
    def __init__(self):
        self.value = 0
    
    def write(self, data):
        self.value = data
        
    def read(self):
        return self.value
    
class Flags:
    def __init__(self):
        self.carry = 0
        self.zero = 0