n = input().strip()
s = set(n)
if any(c not in "2018" for c in n):
    print(0)
elif not set("2018").issubset(s):
    print(1)
else:
    c2 = n.count("2")
    c0 = n.count("0")
    c1 = n.count("1")
    c8 = n.count("8")
    if c2 == c0 == c1 == c8:
        print(8)
    else:
        print(2)
