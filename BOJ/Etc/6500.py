while True:
    n = int(input())
    if n == 0:
        break
    s = set()
    a = n
    while a not in s:
        s.add(a)
        sq = str(a * a).zfill(8)
        a = int(sq[2:6])
    print(len(s))
