for _ in range(int(input())):
    a, b = map(int, input().split())
    s = b * 2 - a
    print(s, b - s)
