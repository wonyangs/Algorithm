n, m = map(int, input().split())

if n > m:
    n, m = m, n

for i in range(n + 1, m + 2):
    print(i)
