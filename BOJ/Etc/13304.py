import math
n, k = map(int, input().split())
groups = [0] * 5
for _ in range(n):
    s, y = map(int, input().split())
    if y <= 2:
        groups[0] += 1
    elif y <= 4:
        groups[1 + s] += 1
    else:
        groups[3 + s] += 1
print(sum(math.ceil(x / k) for x in groups))
