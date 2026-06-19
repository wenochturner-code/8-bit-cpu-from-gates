def bits_to_int(bit):
    integer = 0
    for i in range(8):
        if bit[i] == 1:
            integer += 2**(7-i)
    return integer

def int_to_bits(n):
    if n < 0 or n > 255:
        print("number needs to fit in one byte")
        return [0]*8

    byte = []

    while n > 0:
        remainder = n % 2
        n = n // 2
        byte.append(remainder)

    while len(byte) < 8:
        byte.append(0)

    byte.reverse()

    return byte
    
    