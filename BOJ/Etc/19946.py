n = int(input())
d = (1 << 64) - n
print(64 - d.bit_length() + 1)
