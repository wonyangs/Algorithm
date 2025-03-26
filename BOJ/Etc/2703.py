t = int(input().strip())
for _ in range(t):
    s = input().rstrip()
    r = input().rstrip()
    res = []
    for c in s:
        if c == " ":
            res.append(c)
        else:
            res.append(r[ord(c) - 65])
    print("".join(res))
