N = int(input())
s = int(input())
m = s
r = s < 0
for _ in range(N):
    a, b = map(int, input().split())
    s = a + s - b
    if s < 0:
        r = True
    m = max(m, s)
print(0 if r else m)
