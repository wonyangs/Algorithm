n = int(input())
x = []
y = []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
s = max(max(x) - min(x), max(y) - min(y))
print(s * s)
