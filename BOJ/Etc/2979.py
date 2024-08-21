a, b, c = map(int, input().split())

t = [0] * 101

for _ in range(3):
    s, e = map(int, input().split())
    for i in range(s, e):
        t[i] += 1

cost = 0
for x in t:
    if x == 1:
        cost += a
    elif x == 2:
        cost += b * 2
    elif x == 3:
        cost += c * 3

print(cost)
