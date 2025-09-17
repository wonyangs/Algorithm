n, s = input().split()
n = int(n)
t = 0
for _ in range(n):
    name, q = input().split()
    q = int(q)
    if s in name.split('_'):
        t += q
print(t)
