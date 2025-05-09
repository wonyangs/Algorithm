n, x = map(int, input().split())
s = 0
for p in map(int, input().split()):
    s += p
print(1 if s % x == 0 else 0)
