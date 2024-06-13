import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    M = N
    while N != 1:
        if N % 2 == 0:
            N //= 2
        else:
            N = N * 3 + 1
        M = max(M, N)
    print(M)
