n = int(input())
e = []

for _ in range(n):
    s, t, b = map(int, input().split())
    e.append((s, b))
    e.append((t, -b))

e.sort()

cur = 0
ans = 0

for _, x in e:
    cur += x
    ans = max(ans, cur)

print(ans)
