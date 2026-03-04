import sys

d = sys.stdin.read().split()[1:]
x = []
y = []

for p in d:
    a, b = map(int, p.split(','))
    x.append(a)
    y.append(b)

print(f"{min(x)-1},{min(y)-1}")
print(f"{max(x)+1},{max(y)+1}")
