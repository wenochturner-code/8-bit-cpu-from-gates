def AND(a,b):
    return 1 if a and b else 0

def OR(a,b):
    return 1 if a or b else 0

def NAND(a,b):
    return 0 if a and b else 1

def NOR(a,b):
    return 0 if a or b else 1

def XOR(a,b):
    return 1 if a != b else 0

def NOT(a):
    return 0 if a == 1 else 1

def AND_N(*bits):
    result = 1
    for b in bits:
        result = AND(result, b)
    return result

def OR_N(*bits):
    result = 0
    for b in bits:
        result = OR(result, b)
    return result