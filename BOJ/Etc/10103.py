aa, bb = 100, 100
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a < b:
        aa -= b
    elif a > b:
        bb -= a
print(aa)
print(bb)
