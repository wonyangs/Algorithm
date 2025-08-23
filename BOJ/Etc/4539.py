n = int(input())
for _ in range(n):
    x = int(input())
    p = 10
    while x >= p:
        x = ((x + p // 2) // p) * p
        p *= 10
    print(x)
