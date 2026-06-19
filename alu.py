from gates import AND, OR, XOR, NOT, AND_N
from adders import eight_bit_adder, ones_compliment


'''
  F2 F1 F0   Operation
  0  0  0    Add
  0  0  1    Add with carry
  0  1  0    Subtract
  0  1  1    Subtract with borrow
  1  0  0    Bitwise AND
  1  0  1    Bitwise XOR
  1  1  0    Bitwise OR
  1  1  1    Compare.
'''
def ALU(F2, F1, F0, a, b, carry_in=0):

    ADD    = AND_N(NOT(F2), NOT(F1), NOT(F0))
    ADC    = AND_N(NOT(F2), NOT(F1), F0)
    SUB    = AND_N(NOT(F2), F1, NOT(F0))
    SBB    = AND_N(NOT(F2), F1, F0)
    AND_OP = AND_N(F2, NOT(F1), NOT(F0))
    XOR_OP = AND_N(F2, NOT(F1), F0)
    OR_OP  = AND_N(F2, F1, NOT(F0))
    COMP   = AND_N(F2, F1, F0)

    if ADD:
        return eight_bit_adder(a, b, 0)

    if ADC:
        return eight_bit_adder(a, b, carry_in)

    if SUB:
        return eight_bit_adder(a, ones_compliment(b), 1)

    if SBB:
        return eight_bit_adder(a, ones_compliment(b), carry_in)

    if AND_OP:
        return [AND(a[i], b[i]) for i in range(8)], 0

    if XOR_OP:
        return [XOR(a[i], b[i]) for i in range(8)], 0

    if OR_OP:
        return [OR(a[i], b[i]) for i in range(8)], 0

    if COMP:
        return eight_bit_adder(a, ones_compliment(b), 1)