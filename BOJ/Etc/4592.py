while (s := input()) != '0':
    _, *a = map(int, s.split())
    print(*[x for i, x in enumerate(a) if i == 0 or x != a[i-1]], '$')
