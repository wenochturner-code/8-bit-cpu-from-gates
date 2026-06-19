from gates import AND_N, NOT
from alu import ALU
from registers import Register, Flags
from memory import RAM
from helpers import bits_to_int

class CPU:
    def __init__(self):
        self.A = Register()
        self.A.write([0]*8)
        self.PC = Register()
        self.OUT = Register()
        self.flags = Flags()
        self.ram = RAM(256)
        self.running = True
        self.PC.write(0)
        self.last_op = None
     
    # Opcode = low 3 bits of the byte (b2 b1 b0):
    # Ex: [X,X,X,X,X,b2,b1,b0]
    #   000  (0)  NOP / empty cell
    #   001  (1)  LOAD
    #   010  (2)  STORE
    #   011  (3)  ADD
    #   100  (4)  SUB
    #   101  (5)  JUMP
    #   110  (6)  JZ
    #   111  (7)  HALT
    
    def decode(self, opcode_byte):
        b2, b1, b0 = opcode_byte[5], opcode_byte[6], opcode_byte[7]
        
        if AND_N(NOT(b2),NOT(b1),NOT(b0)):
            return "NOP"
        if AND_N(NOT(b2),NOT(b1), b0):
            return "LOAD"
        if AND_N(NOT(b2),b1,NOT(b0)):
            return "STORE"
        if AND_N(NOT(b2),b1,b0):
            return "ADD"
        if AND_N(b2,NOT(b1),NOT(b0)):
            return "SUB"
        if AND_N(b2,NOT(b1),b0):
            return "JUMP"
        if AND_N(b2,b1,NOT(b0)):
            return "JZ"
        if AND_N(b2,b1,b0):
            return "HALT"
        
    
    def step(self):
        opcode_byte = self.ram.read(self.PC.read())
        operand_byte = self.ram.read(self.PC.read()+1)
        address = bits_to_int(operand_byte)
        
        op = self.decode(opcode_byte)
        
        if op == "NOP":
            print("No machine code")
            self.last_op = None
        
        elif op == "LOAD":
            self.A.write(self.ram.read(address))
            self.last_op = "LOAD"
        
        elif op == "STORE":
            self.ram.write(address, self.A.read())
            self.last_op = "STORE"
        
        elif op == "ADD":
            result, carry = ALU(0, 0, 0, self.A.read(), self.ram.read(address))
            self.A.write(result)
            self.flags.carry = carry
            self.flags.zero = 1 if all(b == 0 for b in result) else 0
            self.last_op = "ADD"
        
        elif op == "SUB":
            result, carry = ALU(0, 1, 0, self.A.read(), self.ram.read(address))
            self.A.write(result)
            self.flags.carry = carry
            self.flags.zero = 1 if all(b == 0 for b in result) else 0
            self.last_op = "SUB"
        
        elif op == "JUMP":
            self.PC.write(address)
            self.last_op = "JUMP"
            return
            
        elif op == "JZ":
            self.last_op = "JZ"
            if self.flags.zero == 1:
                self.PC.write(address)
                return
        
        elif op == "HALT":
            self.running = False
            self.last_op = ("HALT", address)
            return
        
        self.PC.write(self.PC.read() + 2)
    
    def run(self):
        while self.running:
            self.step()
        
        
            
            
            