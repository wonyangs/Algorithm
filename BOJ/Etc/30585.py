N, M = map(int, input().split())
a, b = 0, 0
for _ in range(N):
    s = input()
    a += s.count('1')
    b += s.count('0')
print(min(a, b))
