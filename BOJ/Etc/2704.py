n = int(input())
for _ in range(n):
    t = input().split(':')
    h, m, s = int(t[0]), int(t[1]), int(t[2])
    hb = format(h, '06b')
    mb = format(m, '06b')
    sb = format(s, '06b')
    c = ''
    for i in range(6):
        c += hb[i] + mb[i] + sb[i]
    r = hb + mb + sb
    print(c, r)
