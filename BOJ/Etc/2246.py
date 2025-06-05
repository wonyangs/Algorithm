n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]

lst.sort()
res = 0
min_c = float('inf')

for d, c in lst:
    if c < min_c:
        res += 1
        min_c = c

print(res)
