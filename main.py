from cpu import CPU
from helpers import int_to_bits, bits_to_int

# Opcodes: LOAD=1  STORE=2  ADD=3  SUB=4  JUMP=5  JZ=6  HALT=7

def run_program(label, program, data, result_addr):
    """Fresh CPU -> load program + data -> run -> print the result."""
    cpu = CPU()

    addr = 0
    for opcode, operand in program:                 # 2 cells per instruction
        cpu.ram.write(addr,     int_to_bits(opcode))
        cpu.ram.write(addr + 1, int_to_bits(operand))
        addr += 2

    for address, value in data.items():             # load the data
        cpu.ram.write(address, int_to_bits(value))

    cpu.run()
    print(f"{label} = {bits_to_int(cpu.ram.read(result_addr))}")
    return cpu


# --- programs ---
add_program = [
    (1, 100),   # LOAD  100
    (3, 101),   # ADD   101
    (2, 102),   # STORE 102
    (7, 0),     # HALT
]
add_data = {100: 5, 101: 3}

mul_program = [
    (1, 102),   # LOAD  result
    (3, 100),   # ADD   multiplicand
    (2, 102),   # STORE result
    (1, 101),   # LOAD  counter
    (4, 103),   # SUB   one
    (2, 101),   # STORE counter
    (6, 16),    # JZ    end
    (5, 0),     # JUMP  loop
    (7, 0),     # HALT
]
mul_data = {100: 5, 101: 3, 102: 0, 103: 1}


# --- run them ---
run_program("5 + 3", add_program, add_data, 102)
run_program("5 * 3", mul_program, mul_data, 102)