import sys
r = sys.stdin.readline

n = int(r())
for _ in range(n):
    s = r().strip()
    res = ""
    i = 0
    while i < len(s):
        c = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            c += 1
            i += 1
        res += str(c) + s[i]
        i += 1
    print(res)
