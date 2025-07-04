n = int(input())
a = []

for i in range(1, n + 1):
    s, c, l = map(int, input().split())
    a.append((-s, c, l, i))

a.sort()
print(a[0][3])
