n, p, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if p == q:
    if all(a[i] == b[i] for i in range(n)):
        print("YES")
        print(" ".join(["0"] * n))
    else:
        print("NO")
else:
    d = p - q
    k = []
    ok = True
    
    for i in range(n):
        diff = b[i] - a[i]
        if diff % d != 0:
            ok = False
            break
        ki = diff // d
        if ki < 0 or ki > 10000:
            ok = False
            break
        k.append(ki)
    
    if ok:
        print("YES")
        print(" ".join(map(str, k)))
    else:
        print("NO")
