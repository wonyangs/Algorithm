s = input().strip()
for c in s:
    a = ord(c)
    t = sum(int(x) for x in str(a))
    print(c * t)
