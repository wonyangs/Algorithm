N, M = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(M)]

baskets = list(range(1, N + 1))

for n in arr:
    i, j = n
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

print(*baskets)
