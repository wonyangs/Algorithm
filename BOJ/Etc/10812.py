n, m = map(int, input().split())
baskets = list(range(1, n + 1))

for _ in range(m):
    i, j, k = map(int, input().split())
    baskets[i-1:j] = baskets[k-1:j] + baskets[i-1:k-1]

print(*baskets)
