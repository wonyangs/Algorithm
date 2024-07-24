from itertools import combinations as c
from math import gcd

def l(a, b):
    return a * b // gcd(a, b)

n = list(map(int, input().split()))
m = float('inf')

for x in c(n, 3):
    t = l(l(x[0], x[1]), x[2])
    if t < m:
        m = t

print(m)
