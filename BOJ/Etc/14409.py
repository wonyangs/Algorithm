n = int(input())
x = int(input())
t = 0
for _ in range(n):
    p = list(map(int, input().split()))
    p1, p2 = p[0], p[1]
    if abs(p1 - p2) <= x:
        t += max(p1, p2)
    else:
        p3 = int(input())
        t += p3
print(t)
