import sys
N = int(sys.stdin.readline())
if N == 0:
    print(0)
else:
    L = N.bit_length()
    print(L if N == 1 << (L - 1) else L + 1)
