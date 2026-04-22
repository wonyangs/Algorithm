c, m = input().split()
r = ""
if c == 'E':
    p = m[0]
    n = 0
    for x in m:
        if x == p:
            n += 1
        else:
            r += p + str(n)
            p = x
            n = 1
    r += p + str(n)
else:
    for i in range(0, len(m), 2):
        r += m[i] * int(m[i+1])
print(r)
