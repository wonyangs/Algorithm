import math
n = int(input())
c = list(map(float, input().split()))
v = sum([x**3 for x in c])
res = math.pow(v, 1/3)
print(res)
