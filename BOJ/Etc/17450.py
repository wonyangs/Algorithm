p1, w1 = map(int, input().split())
p2, w2 = map(int, input().split())
p3, w3 = map(int, input().split())
best = ''
bv = 0
for n, (p, w) in zip('SNU', [(p1, w1), (p2, w2), (p3, w3)]):
    c = p * 10 - (500 if p * 10 >= 5000 else 0)
    v = w * 10 / c
    if v > bv:
        bv = v
        best = n
print(best)
