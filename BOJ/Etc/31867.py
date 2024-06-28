input()
a, b = 0, 0
for c in input():
    if int(c) % 2 == 0:
        a += 1
    else:
        b += 1
if a == b:
    print(-1)
elif a > b:
    print(0)
else:
    print(1)
