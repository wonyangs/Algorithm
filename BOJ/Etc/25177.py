n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

k = max(n, m)
if len(a) < k:
    a += [0] * (k - len(a))
if len(b) < k:
    b += [0] * (k - len(b))

ans = max(0, max(b[i] - a[i] for i in range(k)))
print(ans)
