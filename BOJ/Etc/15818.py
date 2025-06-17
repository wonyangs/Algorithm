n, m = map(int, input().split())
a = list(map(int, input().split()))
p = 1
for x in a:
    p = (p * x) % m
print(p)
