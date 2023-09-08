n, d = map(int, input().split())
res = 0
for i in range(1, n+1):
    res += str(i).count(str(d))
print(res)
