N = int(input())
s = [[0, 0, 0] for _ in range(3)]
for _ in range(N):
    a, b, c = map(int, input().split())
    for i, x in enumerate([a, b, c]): s[i][0] += x; s[i][1] += x == 3; s[i][2] += x == 2
m = max(s)[0]
c = [i for i in range(3) if s[i][0] == m]
c = c if len(c) == 1 else [i for i in c if s[i][1] == max(s[x][1] for x in c)]
c = c if len(c) == 1 else [i for i in c if s[i][2] == max(s[x][2] for x in c)]
print(c[0] + 1 if len(c) == 1 else 0, m)
