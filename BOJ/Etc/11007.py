import sys

d = sys.stdin.read().split()
if d:
    p = 1
    for _ in range(int(d[0])):
        n = int(d[p])
        p += 1
        a = list("abcdefghijklmnopqrstuvwxyz")
        s = ""
        for _ in range(n):
            c = a.pop(int(d[p]))
            s += c
            a.insert(0, c)
            p += 1
        print(s)
