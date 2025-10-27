n = int(input())
x, y, r = map(int, input().split())
a = 0
b = 0
for _ in range(n):
    t = int(input())
    d = abs(x - t)
    if d < r:
        a += 1
    elif d == r:
        b += 1
print(a, b)
