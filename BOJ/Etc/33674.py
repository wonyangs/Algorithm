n, d, k = map(int, input().split())
s = list(map(int, input().split()))
m = max(s)
t = k // m
print((d - 1) // t)
