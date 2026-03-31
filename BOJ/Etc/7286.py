import sys

D = sys.stdin.read().split()
if D:
    T = int(D[0])
    p = 1
    for _ in range(T):
        n = int(D[p])
        p += 1
        C = [0] * 1005
        for _ in range(n):
            a = int(D[p+1])
            b = int(D[p+2])
            for i in range(a, b):
                C[i] += 1
            p += 3
        print("".join(chr(64 + c) for c in C if c > 0))
