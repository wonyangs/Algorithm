alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    t = set()
    for a in alpha:
        t.add(a)
    s = input()
    for c in s:
        if c in t:
            t.remove(c)
    res = 0
    for a in t:
        res += ord(a)
    print(res)
