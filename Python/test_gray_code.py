print('0' * 3)
N = 2
print(N & 2)
if N & 2 == 1:
    print('1')

code_list = [bytearray(b'0'*N)] * (2**N)

def num_to_blist(num, length):
    blist = [0] * length
    for i in range(length):
        if num & (2**i) > 0:
            blist[length-1-i] = 1
    return blist

def num_to_glist(num, length):
    blist = [0] * length
    for i in range(length):
        if num & (2**i) > 0:
            blist[length-1-i] = 1
    blist_rightshift = [0] + blist[:-1]
    # XOR
    glist = [ blist[i] ^ blist_rightshift[i] for i in range(length)]
    return glist

gray_code_list = [ num_to_glist(i, N)  for i in range(2**N)]
print(gray_code_list)

byte_code = N.to_bytes(4, 'big')
print(byte_code)


