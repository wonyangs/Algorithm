a, b = map(int, input().split())
c, d = map(int, input().split())

i, j, k, l = a/c + b/d, c/d + a/b, d/b + c/a, b/a + d/c
m = max(i, j, k, l)
if m == i:
    print(0)
elif m == j:
    print(1)
elif m == k:
    print(2)
else:
    print(3)
