import sys

d = list(map(int, sys.stdin.read().split()))
j, r = d[0], d[1]
s = [0] * j

for i in range(j * r):
    s[i % j] += d[i + 2]

w = 0
for i in range(j):
    if s[i] >= s[w]:
        w = i

print(w + 1)
