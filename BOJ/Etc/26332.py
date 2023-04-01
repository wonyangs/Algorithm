for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a, b)
    print(b + (b - 2) * (a - 1))
