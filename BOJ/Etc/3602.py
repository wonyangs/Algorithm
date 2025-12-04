b, w = map(int, input().split())
for n in range(200, 0, -1):
    h = n * n // 2
    if n % 2 == 0:
        if b >= h and w >= h:
            print(n)
            break
    else:
        l = h + 1
        if (b >= l and w >= h) or (w >= l and b >= h):
            print(n)
            break
else:
    print("Impossible")
