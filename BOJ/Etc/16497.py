n = int(input())
a = []
for _ in range(n):
    s, t = map(int, input().split())
    a += ((s, 1), (t, -1))
k = int(input())
a.sort()
c = 0
r = 1
for _, d in a:
    c += d
    if c > k:
        r = 0
        break
print(r)
