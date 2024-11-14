import sys
n = int(sys.stdin.read())
p = 10
while n >= p:
    n = (n + p // 2) // p * p
    p *= 10
print(n)
