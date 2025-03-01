n, a, b = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
s = g[a-1][b-1]
res = "HAPPY"
for j in range(n):
    if j != b-1 and g[a-1][j] > s:
        res = "ANGRY"
        break
if res == "HAPPY":
    for i in range(n):
        if i != a-1 and g[i][b-1] > s:
            res = "ANGRY"
            break
print(res)
