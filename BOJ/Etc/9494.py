while True:
    n = int(input())
    if n == 0:
        break
    a = [input() for _ in range(n)]
    c = next(i for i, ch in enumerate(a[0]) if ch != ' ')
    for ln in a:
        while c < len(ln) and ln[c] != ' ':
            c += 1
    print(c + 1)
