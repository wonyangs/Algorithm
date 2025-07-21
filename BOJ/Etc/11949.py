n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
for i in range(1, m+1):
    for j in range(n-1):
        if a[j] % i > a[j+1] % i:
            a[j], a[j+1] = a[j+1], a[j]
for x in a:
    print(x)
