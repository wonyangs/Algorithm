for _ in range(int(input())):
    d, n, s, p = map(int, input().split())
    a = n * s
    b = n * p + d
    if a == b:
        print("does not matter")
    elif a < b:
        print("do not parallelize")
    else:
        print("parallelize")
