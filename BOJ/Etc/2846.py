n = int(input())
h = list(map(int, input().split()))

m = 0
c = 0

for i in range(1, n):
    if h[i] > h[i-1]:
        c += h[i] - h[i-1]
        m = max(m, c)
    else:
        c = 0

print(m)
