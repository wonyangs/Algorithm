from math import ceil
K, N = map(int, input().split())
if N == 1:
    print(-1)
    exit(0)

if N * K % (N - 1) == 0:
    print(N * K // (N - 1))
else:
    print(N * K // (N - 1) + 1)
