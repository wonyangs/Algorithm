e, f, c = map(int, input().split())
b = e + f
d = 0

while b >= c:
    n = b // c
    d += n
    b = n + (b % c)

print(d)
