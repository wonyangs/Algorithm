n = int(input())
if n == 0:
    print(1)
    exit()
L = len(str(n))
for k in range(L, 0, -1):
    for d in range(1, 10):
        if int(str(d) * k) <= n:
            print(k)
            exit()
