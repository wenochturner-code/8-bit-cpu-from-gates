from gates import AND, OR, XOR, NOT, AND_N, OR_N

def half_adder(a,b):
    sum_out = XOR(a,b)
    carry_out = AND(a,b)
    return sum_out, carry_out

def full_adder(a,b, carry_in):
    sum1, carry1 = half_adder(a,b)
    sum2, carry2 = half_adder(carry_in, sum1)
    carry_out = OR(carry2, carry1)
    return sum2, carry_out

def eight_bit_adder(a,b, carry_in):
    sum0, carry0 = full_adder(a[7],b[7], carry_in)
    sum1, carry1 = full_adder(a[6],b[6],carry0)
    sum2, carry2 = full_adder(a[5],b[5],carry1)
    sum3, carry3 = full_adder(a[4],b[4],carry2)
    sum4, carry4 = full_adder(a[3],b[3],carry3)
    sum5, carry5 = full_adder(a[2],b[2],carry4)
    sum6, carry6 = full_adder(a[1],b[1],carry5)
    sum7, carry7 = full_adder(a[0],b[0],carry6)
    return [sum7, sum6, sum5, sum4, sum3, sum2, sum1, sum0], carry7

def ones_compliment(a):
    return [NOT(bit) for bit in a]