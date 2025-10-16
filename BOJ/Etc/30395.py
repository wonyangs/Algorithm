n = int(input())
p = list(map(int, input().split()))
s = m = 0
h = 1
g = -1

for i in range(n):
    if g == i:
        h = 1
    if p[i] == 0:
        if h:
            h = 0
            g = i + 2
        else:
            s = 0
    else:
        s += 1
        m = max(m, s)

print(m)
