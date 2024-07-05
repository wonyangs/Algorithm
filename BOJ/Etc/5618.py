import math

input()
num = math.gcd(*map(int, input().split()))

res = []
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        res.append(i)
        if i != num // i:
            res.append(num // i)
res.sort()

for i in res:
    print(i)
