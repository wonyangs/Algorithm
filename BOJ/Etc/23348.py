x, y, z = map(int, input().split())
N = int(input())
M = 0
for _ in range(N):
    cnt = 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        cnt += a * x + b * y + c * z
    M = max(M, cnt)
print(M)
