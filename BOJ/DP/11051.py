N, K = map(int, input().split())
a, b = [1, 1], []
for _ in range(N-1):
    before = 0
    b.append(1)
    for i in range(len(a) - 1):
        b.append((a[i] + a[i+1]) %10007)
    b.append(1)
    a, b = b, []
print(a[K])
