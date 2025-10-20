while True:
    c, w, l, p = map(int, input().split())
    if c == 0 and w == 0 and l == 0 and p == 0:
        break
    print(c ** (w * l * p))
