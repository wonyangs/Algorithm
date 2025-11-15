n = [int(input()) & 15 for _ in range(3)]
print(str(int(''.join(bin(x)[2:].zfill(4) for x in n), 2)).zfill(4))
