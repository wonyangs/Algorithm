n, k = map(int, input().split())
a = list(map(int, input().split()))
c = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == k:
            c += 1
print(c)
