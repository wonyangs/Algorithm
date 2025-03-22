def period(s):
    l = len(s)
    for i in range(1, l + 1):
        if l % i == 0:
            if s[:i] * (l // i) == s:
                return s[:i]
    return s

t = int(input())
for _ in range(t):
    w = input()
    n = len(w)

    a = ''
    for i in range(n):
        a += w[(2 * i) % n]

    b = ''
    for i in range(n):
        b += w[(2 * i + 1) % n]

    print(period(a))
    print(period(b))
