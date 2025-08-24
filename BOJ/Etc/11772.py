n = int(input())
s = 0
for _ in range(n):
    p = input().strip()
    b, e = int(p[:-1]), int(p[-1])
    s += b ** e
print(s)
