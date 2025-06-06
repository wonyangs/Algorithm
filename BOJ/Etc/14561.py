T = int(input())
for _ in range(T):
    a, n = map(int, input().split())
    d = []
    x = a
    while x:
        d.append(x % n)
        x //= n
    if d == d[::-1]:
        print(1)
    else:
        print(0)
