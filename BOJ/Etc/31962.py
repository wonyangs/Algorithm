N, X = map(int, input().split())
m = -1
for _ in range(N):
    a, b = map(int, input().split())
    if a + b <= X:
        m = max(m, a)
print(m)
