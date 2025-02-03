N, M = map(int, input().split())
fc = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    fc[a - 1] += 1; fc[b - 1] += 1
print(*fc, sep='\n')
