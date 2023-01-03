c, k, p = map(int, input().split())
res = 0
for n in range(c + 1):
    res += k * n + p * n ** 2
print(res)
