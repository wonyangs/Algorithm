N = int(input())
arr = []
for _ in range(N):
    a, d, g = map(int, input().split())
    res = a * (d + g)
    if a == d + g:
        res *= 2
    arr.append(res)
print(max(arr))
