t = int(input())
for _ in range(t):
    n = int(input())
    r = 1
    for i in range(1, n + 1):
        r *= i
        while r % 10 == 0:
            r //= 10
        r %= 1000000000000
    print(r % 10)
