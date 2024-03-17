while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if a == b:
        print(a)
    else:
        print(2 * a - b)
