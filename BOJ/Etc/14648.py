n, q = map(int, input().split())
x = list(map(int, input().split()))
for _ in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        a, b = t[1], t[2]
        s = sum(x[a-1:b])
        print(s)
        x[a-1], x[b-1] = x[b-1], x[a-1]
    else:
        a, b, c, d = t[1], t[2], t[3], t[4]
        s1 = sum(x[a-1:b])
        s2 = sum(x[c-1:d])
        print(s1 - s2)
