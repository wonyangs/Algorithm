for _ in range(int(input())):
    p, m = map(int, input().split())
    s, r = set(), 0
    for _ in range(p):
        x = int(input())
        if x in s:
            r += 1
        else:
            s.add(x)
    print(r)
