n, k = map(int, input().split())
for _ in range(n):
    r = input().split()
    e = []
    for p in r:
        e += [p] * k
    for _ in range(k):
        print(" ".join(e))
