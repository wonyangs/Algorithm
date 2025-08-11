while True:
    try:
        m, p, l, e, r, s, n = map(int, input().split())
    except:
        break
    for _ in range(n):
        m, p, l = p // s, l // r, m * e
    print(m)
